from pymongo import MongoClient
# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["edugraph"]
collection_etudiants = db["etudiants"]

# Requête 1 : Trouver tous les étudiants
etudiants = collection_etudiants.find()
for etudiant in etudiants:
    print(etudiant)

# Requête 2 : Trouver un etudiant par son nom
print("="*100)
nom_etudiant = "PILI"
etudiant = collection_etudiants.find_one({"nom": nom_etudiant})
print(etudiant)

# Requête 3 : Trouver les étudiants ayant une compétence spécifique
print("="*100)
competence = "Python"   
etudiants_python = collection_etudiants.find({"competences": competence})
for etudiant in etudiants_python:
    print(etudiant)