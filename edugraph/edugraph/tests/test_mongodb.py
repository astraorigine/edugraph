from sprint3_integration.config import MONGO_URI, NEO4J_URI, NEO4J_PASSWORD, NEO4J_USER
from pymongo import MongoClient


client = MongoClient(MONGO_URI)     
db = client["edugraph"]


#Test 1: Connexion fonctionnelle à MongoDB
def test_connection_mongodb():
    assert db.name =="edugraph"

# Test 2 :La collection étudiants existe et contient des données
def test_collection_etudiants_non_vide():
    count = db["etudiants"].count_documents({})
    assert count >0

# Test 3 : Un étudiant possède les champs obligatoires
def test_structure_etudiant():
    etudiant = db["etudiants"].find_one({"email":"alice@edugraph.com"})
    assert etudiant is not None
    assert "nom" in etudiant
    assert "email" in etudiant
    assert "competences" in etudiant
    assert "niveau" in etudiant