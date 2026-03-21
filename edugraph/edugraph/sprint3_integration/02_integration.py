from pymongo import MongoClient
from neo4j import GraphDatabase

#connexion à la base de données MongoDB
client = MongoClient("mongodb://localhost:27017/")
db= client["edugraph"]

#connexion à la base de données Neo4j
driver =GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","Tanjiro12"))

def executer_cypher(requete,parametres={}):
    with driver.session() as session:
        resultat = session.run(requete, parametres)
        return resultat.data()


def synchroniser_etudiant(email):
    # 1. Récuperation de l'etudiant  par l'email dans MongoDB
    etudiant = db["etudiants"].find_one({"email": email})
    
    if not etudiant:
        print(f" Étudiant {email} introuvable dans MongoDB")
        return

    print(f" Étudiant trouvé : {etudiant['nom']}")
    
    # 2.Creation du noeud Neo4j pour l'etudiant
    executer_cypher("""
        MERGE (e:Etudiant {email: $email})
        SET e.nom = $nom
        SET e.niveau = $niveau
        SET e.filiere = $filiere
    """, {
        "email": etudiant["email"],
        "nom": etudiant["nom"],
        "niveau": etudiant["niveau"],
        "filiere": etudiant["filiere"]
    })
    print(f" Nœud Neo4j créé/mis à jour pour {etudiant['nom']}")