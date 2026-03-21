from pymongo import MongoClient
from neo4j import GraphDatabase
import pytest

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db=client["edugraph"]
# Connexion à Neo4j
driver = GraphDatabase.driver("bolt://localhost:7687/",auth=("neo4j","Tanjiro12"))


def executer_cypher(requete,parametres=({})):
    with driver.session() as session:
        resultat = session.run(requete,parametres)
        return resultat.data()
    
# Test 1: Vérifier que les étudiants de MongoDB sont synchronisés avec Neo4j
def test_etudiant_synchronise():
    # Récupérer les étudiants de MongoDB
    etudiant =db["etudiants"].find_one({"email":"alice@edugraph.com"})
    # Vérifier que l'étudiant existe dans Neo4j
    resultat = executer_cypher("MATCH (e:Etudiant{email:$email}) RETURN e",{"email":etudiant["email"]})
    # Vérifier que les données de l'étudiant sont synchronisées
    assert etudiant["email"] == resultat[0]["e"]["email"]
    assert etudiant["nom"] == resultat[0]["e"]["nom"] 