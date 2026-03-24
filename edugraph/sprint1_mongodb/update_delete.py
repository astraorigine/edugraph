from pymongo import MongoClient

#connexion à MongoDB
client= MongoClient("mongodb://localhost:27017/")
db=client["edugraph"]
collection_etudiants= db["etudiants"]

#Mettre à jour 
new_value= "kahedehokazuha@gmail.com"
nom_etudiant= "Ibara"
resultat_update= collection_etudiants.update_one(
    {"nom":nom_etudiant},
    {"$set":{"email":new_value}}
)

print(f"Nombre de documents modifiés: {resultat_update.modified_count}")


#supprimer un document
nom_etudiant_supprimer= "Ibara"
resultat_update= collection_etudiants.delete_one({"nom":nom_etudiant_supprimer})

print(f"Nombre de documents supprimés: {resultat_update.deleted_count}")
print(collection_etudiants.find_one({"nom":nom_etudiant_supprimer}))

