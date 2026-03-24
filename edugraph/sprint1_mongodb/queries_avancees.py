from pymongo import MongoClient

# Connexion à MongoDB
client= MongoClient("mongodb://localhost:27017/")
db= client["edugraph"]
collection_etudiants= db["etudiants"]



#Trouver un etudiant dasns l'age est superieur à 20 ans
age=20
etudiants_ages= collection_etudiants.find({"age":{"$gt":age}})
print(f"Etudiants avec age superieur à {age} ans:")
for etudiant in etudiants_ages:
    print(f"Nom: {etudiant['nom']}, Age: {etudiant['age']}")



print("Trouver les etudiants avec une caractéristique faisant partie d'une liste")
competences= ["ML", "Python"]
etudiant_competences= collection_etudiants.find({"competences":{"$in":competences}})
print(f"Etudiants avec les competences {competences}:")
for etudiant in etudiant_competences:
    print(f"Etudiant: {etudiant['nom']}, Competences: {etudiant['competences']}")

#Trouve les étudiants de niveau M1 ET qui connaissent Python
niveau = "Licence3"
competence = "Python"
etudiants_niveau_competence = collection_etudiants.find(
    {"$and": [
        {"niveau": niveau},
        {"competences":competence}
    ]}
)
print(f"Etudiants de niveau {niveau} et connaissant {competence}:")
for etudiant in etudiants_niveau_competence:
    print(f"Etudiant: {etudiant['nom']}, Niveau: {etudiant['niveau']}, Competences: {etudiant['competences']}")

#Recherche textuelle
print("Recherche textuelle pour trouver les étudiants dont l'email contient '")
texte_recherche = "pili@gmail.com"
etudiants_email = collection_etudiants.find({"email":{"$regex": texte_recherche}})

for etudiant in etudiants_email:
    print(f"Etudiant: {etudiant['nom']}, Email: {etudiant['email']}")