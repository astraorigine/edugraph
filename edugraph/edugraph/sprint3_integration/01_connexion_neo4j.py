from pymongo import MongoClient
from neo4j import GraphDatabase
#connexion à la base de données MongoDB
client = MongoClient("mongodb://localhost:27017/")
db= client["edugraph"]

#connexion à la base de données Neo4j
driver = GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","originel1227"))

driver.verify_connectivity()
print("Connexion réussie à Neo4j")