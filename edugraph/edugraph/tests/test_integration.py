
from sprint3_integration.config import MONGO_URI, NEO4J_URI, NEO4J_PASSWORD, NEO4J_USER
from pymongo import MongoClient
from neo4j import GraphDatabase

client = MongoClient(MONGO_URI)       
db = client["edugraph"]

driver = GraphDatabase.driver(
    NEO4J_URI,                       
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

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