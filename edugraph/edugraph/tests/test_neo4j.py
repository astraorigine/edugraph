from sprint3_integration.config import MONGO_URI, NEO4J_URI, NEO4J_PASSWORD, NEO4J_USER
from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    NEO4J_URI,                         
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

def executer_cypher(requete,parametres=({})):
    with driver.session() as session:
        resultat = session.run(requete,parametres)
        return resultat.data()


# Test 1 connexion à la base de données neo4j
def test_connexion_neo4j():
    driver.verify_connectivity()

# Test 2 Les noeuds étudiant  existent dans la base de données neo4j
def test_noeuds_etudiant_existent():
    resultat = executer_cypher("MATCH (e:Etudiant) RETURN COUNT(e) AS Total")
    assert resultat[0]["Total"]>0

# Test 3 verification que la relation "CONNAIT" existe
def test_relation_CONNAIT_existe():
    resultat = executer_cypher("MATCH ()-[r:CONNAIT]->() RETURN COUNT(r) AS Total")
    assert resultat[0]["Total"]>0