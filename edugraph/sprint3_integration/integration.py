from sprint3_integration.config import MONGO_URI, NEO4J_URI, NEO4J_PASSWORD, NEO4J_USER
from pymongo import MongoClient
from neo4j import GraphDatabase

#connexion à la base de données MongoDB
client = MongoClient(MONGO_URI)
db= client["edugraph"]

#connexion à la base de données Neo4j
driver =GraphDatabase.driver(NEO4J_URI,auth=(NEO4J_USER, NEO4J_PASSWORD))

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

    # 3. Création des relations avec les competences de l'etudiant
    for competence in etudiant["competences"]:
        executer_cypher("""
            Merge(e:Etudiant{email:$email})
            Merge(c:Competence{nom:$competence})
            Merge(e)-[:CONNAIT]->(c)
        """, {
            "email": etudiant["email"],
            "competence": competence
        })


#Synchroniser tous les étudiants de MongoDB vers Neo4j
def synchroniser_tous():
    etudiants = db["etudiants"].find()
    for etudiant in etudiants:
        synchroniser_etudiant(etudiant["email"])
    print("=="*25)
    print("Synchronisation terminée pour tous les étudiants.")

if __name__ == "__main__":
    synchroniser_tous()