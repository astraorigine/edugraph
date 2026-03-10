from pymongo import MongoClient

#connexion à la base de données
client= MongoClient("mongodb://localhost:27017/")
db=client["edugraph"]

print(f"Connexion établit avec succès à la base de données {db.name}")