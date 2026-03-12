from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["edugraph"]

# les collections 

#Suppression des anciens collections.  
collection_etu = db["etudiants"].drop()
collection_cours = db["cours"].drop( )
collection_filiere = db["filiere"].drop( )


# Nouvelle données 
#=================================Filieres
filieres =  [
    {"nom": "Informatique", "niveau": "Licence", "duree": 3},
    {"nom": "Data Science", "niveau": "Master", "duree": 2},
    {"nom": "Cybersécurité", "niveau": "Master", "duree": 2},
    {"nom": "Génie Logiciel", "niveau": "Licence", "duree": 3},
]

#=================================Cours
cours =[
    {
        "titre": "Introduction à Python",
        "filiere": "Informatique",
        "niveau": "L1",
        "competences_apportees": ["Python", "Algorithmique"],
        "prerequis": []
    },
    {
        "titre": "Bases de données SQL",
        "filiere": "Informatique",
        "niveau": "L2",
        "competences_apportees": ["SQL", "Modélisation"],
        "prerequis": ["Algorithmique"]
    },
    {
        "titre": "Machine Learning",
        "filiere": "Data Science",
        "niveau": "M1",
        "competences_apportees": ["Machine Learning", "Scikit-learn"],
        "prerequis": ["Python", "SQL", "Statistiques"]
    },
    {
        "titre": "Deep Learning",
        "filiere": "Data Science",
        "niveau": "M2",
        "competences_apportees": ["Deep Learning", "TensorFlow", "PyTorch"],
        "prerequis": ["Machine Learning", "Python"]
    },
    {
        "titre": "NoSQL & Big Data",
        "filiere": "Data Science",
        "niveau": "M1",
        "competences_apportees": ["MongoDB", "Cassandra", "Hadoop"],
        "prerequis": ["SQL", "Python"]
    },
    {
        "titre": "Sécurité des réseaux",
        "filiere": "Cybersécurité",
        "niveau": "M1",
        "competences_apportees": ["Firewall", "Cryptographie", "Linux"],
        "prerequis": ["Réseaux"]
    },
    {
        "titre": "Développement Web",
        "filiere": "Génie Logiciel",
        "niveau": "L2",
        "competences_apportees": ["JavaScript", "HTML/CSS", "React"],
        "prerequis": ["Algorithmique"]
    },
    {
        "titre": "DevOps & Cloud",
        "filiere": "Génie Logiciel",
        "niveau": "M1",
        "competences_apportees": ["Docker", "Kubernetes", "CI/CD"],
        "prerequis": ["Linux", "Python"]
    },
]

#=================================Etudiants
etudiants = [
    {
        "nom": "Alice Mbeki",
        "age": 22,
        "email": "alice@edugraph.com",
        "filiere": "Data Science",
        "niveau": "M1",
        "competences": ["Python", "SQL", "Machine Learning", "Statistiques"],
        "cours_suivis": ["Introduction à Python", "Bases de données SQL", "Machine Learning"],
        "note_moyenne": 15.5
    },
    {
        "nom": "Bob Diallo",
        "age": 23,
        "email": "bob@edugraph.com",
        "filiere": "Génie Logiciel",
        "niveau": "M1",
        "competences": ["Python", "JavaScript", "Docker", "Linux", "React"],
        "cours_suivis": ["Introduction à Python", "Développement Web", "DevOps & Cloud"],
        "note_moyenne": 14.0
    },
    {
        "nom": "Carol Nzinga",
        "age": 21,
        "email": "carol@edugraph.com",
        "filiere": "Informatique",
        "niveau": "L3",
        "competences": ["Python", "SQL", "Algorithmique", "Modélisation"],
        "cours_suivis": ["Introduction à Python", "Bases de données SQL"],
        "note_moyenne": 16.0
    },
    {
        "nom": "David Konan",
        "age": 24,
        "email": "david@edugraph.com",
        "filiere": "Data Science",
        "niveau": "M2",
        "competences": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "SQL"],
        "cours_suivis": ["Introduction à Python", "Machine Learning", "Deep Learning"],
        "note_moyenne": 17.0
    },
    {
        "nom": "Eva Mensah",
        "age": 22,
        "email": "eva@edugraph.com",
        "filiere": "Cybersécurité",
        "niveau": "M1",
        "competences": ["Linux", "Cryptographie", "Firewall", "Réseaux"],
        "cours_suivis": ["Sécurité des réseaux"],
        "note_moyenne": 15.0
    },
    {
        "nom": "Frank Osei",
        "age": 23,
        "email": "frank@edugraph.com",
        "filiere": "Data Science",
        "niveau": "M1",
        "competences": ["Python", "MongoDB", "SQL", "Hadoop"],
        "cours_suivis": ["Introduction à Python", "NoSQL & Big Data"],
        "note_moyenne": 13.5
    },
    {
        "nom": "Grace Touré",
        "age": 20,
        "email": "grace@edugraph.com",
        "filiere": "Informatique",
        "niveau": "L2",
        "competences": ["Python", "Algorithmique", "HTML/CSS"],
        "cours_suivis": ["Introduction à Python", "Développement Web"],
        "note_moyenne": 14.5
    },
    {
        "nom": "Hugo Bamba",
        "age": 25,
        "email": "hugo@edugraph.com",
        "filiere": "Génie Logiciel",
        "niveau": "M2",
        "competences": ["Docker", "Kubernetes", "Python", "CI/CD", "Linux", "JavaScript"],
        "cours_suivis": ["DevOps & Cloud", "Développement Web"],
        "note_moyenne": 16.5
    },
]


# Insertion des données dans les collections
collection_filiere = db["filiere"]
collection_cours = db["cours"]
collection_etu = db["etudiants"]

collection_filiere.insert_many(filieres)
collection_cours.insert_many(cours)        
collection_etu.insert_many(etudiants)

print(f"Nombre de filières insérées : {collection_filiere.count_documents({})}")
print(f"Nombre de cours insérés : {collection_cours.count_documents({})}")
print(f"Nombre d'étudiants insérés : {collection_etu.count_documents({})}")