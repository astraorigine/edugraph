from pymongo import MongoClient
#connexion à la base de données
client= MongoClient("mongodb://localhost:27017/")
db=client["edugraph"]

collection_etudiants=db["etudiants"]

#Données de l'étudiant à insérer
etudiants = [
        {
        "nom": "PILI",
        "Prenom":"Emmanuel",
        "age": 23,
        "email": "emmanuelpili@gmail.com",
        "filiere":"informatique",
        "competences": ["Java", "Python", "Docker"],
        "niveau": "Licence3"
    },
    {
        "nom": "ITOUA",
        "Prenom":"Ruth",
        "age": 21,
        "email": "itouaruth@gmail.com",
        "filiere":"informatique",
        "competences": ["MongoDB", "JavaScript"],
        "niveau": "L3"
    },
    {
        "nom": "GAKALI",
        "Prenom":"Djio",
        "age": 24,
        "email": "gakalidjio@gmail.com",
        "filiere":"informatique",
        "competences": ["Python", "Machine Learning", "SQL"],
        "niveau": "M2"
    }

]

#insertion de l'étudiant dans la collection
resultat = collection_etudiants.insert_many(etudiants)
print(f"\n IDs inséréscls : {resultat.inserted_ids}")