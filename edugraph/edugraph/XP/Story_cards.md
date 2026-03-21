# Edugraph-Story\_cards:
## Sprint 1


### US-01:Cr�er un profil �tudiant



#### Status : Done



#### Crit�res:



* \[x] Document ins�rer
* \[x] Contient nom, age, email, comp�tences, niveau
* \[x] MongoDB retourne un \_id unique







### US-02 � Ins�rer plusieurs �tudiants

#### Statut : DONE

#### Crit�res :

* &nbsp;\[x] insert\_many fonctionne avec une liste
* &nbsp;\[x] Chaque document a une structure flexible
* &nbsp;\[x] Tous les IDs sont retourn�s





### US-03 � En tant que formateur, je veux trouver des �tudiants selon des crit�res pr�cis.



#### Statut : Done

#### Crit�res :

* \[x]�R�cup�rer tous les �tudiants
* \[X]�Trouver un �tudiant par son nom
* \[x]�Trouver tous les �tudiants qui ma�trisent "Python"


### US-04 — Mettre à jour et supprimer
####Statut : DONE
####Critères :
  - [x] Modification d'un champ sans écraser le tout
  - [x] Supprime un document ciblé
  - [x] Vérification avec find_one après chaque opération

## Sprint2
### US-05 - Créer des noeuds et relations Neo4j

### US-06 - chemin de competences
#### Statut : DONE
#### Critères :
  - [x] Traversée de graphe avec [:EST_PREREQUIS*]
  - [x] Capture du chemin complet avec p =
  - [x] Extraction des nœuds avec nodes(p)

### US-07 — Recommander des étudiants
#### Statut : DONE
#### Critères :
  - [x] MATCH avec relation CONNAIT
  - [x] Filtrage par compétence
  - [x] Retour des propriétés avec e.nom


### US-08 — Synchronisation MongoDB ↔ Neo4j
#### Statut : DONE
#### Critères :
  - [x] Lecture d'un étudiant depuis MongoDB
  - [x] Création de nœud Neo4j avec MERGE
  - [x] Création de relations "CONNAIT" automatiquement 
  - [x] Synchronisation de toute la base







