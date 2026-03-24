#  EduGraph

> Plateforme intelligente de gestion des compétences et parcours d'apprentissage

## Problème résolu
Les établissements scolaires peinent à suivre les compétences de leurs 
étudiants, former des équipes équilibrées et personnaliser les parcours 
de formation.

## Fonctionnalités
-  Recommandation de cours selon le profil étudiant
-  Constitution automatique d'équipes performantes
-  Identification des étudiants pouvant s'entraider
-  Visualisation du chemin de compétences vers un objectif

##  Technologies
| Technologie | Rôle |

| **MongoDB** | Stockage des profils étudiants |
| **Neo4j**   | Modélisation des relations compétences/étudiants |
| **Python**  | Intégration et logique métier |
| **XP + Git**| Méthode de développement agile |

##  Structure du projet
```
edugraph/
├── sprint1_mongodb/      # CRUD et requêtes MongoDB 
├── sprint2_neo4j/        # Modélisation graphe Neo4j
├── sprint3_integration/  # Intégration MongoDB ↔ Neo4j
├── XP/                   # Story Cards et documentation XP
├── VISION.md             # Vision et contexte du projet
├── ARCHITECTURE.md       # Architecture technique
└── README.md             # Ce fichier
```

##  Installation
```bash
# 1. Cloner le projet
git clone https://github.com/astraorigine/edugraph.git
cd edugraph

# 2. Installer les dépendances Python
pip install pymongo neo4j rich

# 3. Démarrer MongoDB (local)
mongod

# 4. Démarrer Neo4j Desktop
# Ouvrir Neo4j Desktop et démarrer la base "edugraph"

# 5. Peupler la base MongoDB
python sprint1_mongodb/06_seed_data.py
```

## Utilisateurs cibles
- Étudiants, Formateurs, Admins, Directeurs d'établissement

## Contexte d'application
- Universités, Grandes écoles, Centres de formation, Bootcamps