#  EduGraph — Vision du projet

## Le problème
Les établissements scolaires ont du mal à :
- Suivre les compétences réelles de chaque étudiant
- Former des groupes de travail équilibrés et performants
- Guider chaque étudiant vers le bon parcours de formation
- Identifier qui peut aider qui dans une promotion

## La solution — EduGraph
EduGraph est une plateforme intelligente de gestion des compétences 
et des parcours d'apprentissage. Elle permet de :
- Recommander les cours adaptés à chaque étudiant
- Constituer des équipes équilibrées automatiquement
-  Identifier les étudiants pouvant s'entraider
-  Visualiser le chemin de compétences vers un objectif

## Les utilisateurs
| Utilisateur    | Besoin |

| **Étudiant**   | Savoir quoi apprendre ensuite |
| **Formateur**  | Suivre la progression de sa classe |
| **Admin**      | Gérer les profils et les parcours |
| **Directeur**  | Vue globale sur les compétences de l'établissement |

## Contexte d'application
- Universités et grandes écoles
- Centres de formation professionnelle
- Bootcamps et écoles du numérique

## Les bénéfices concrets
-  Réduction du temps de constitution d'équipes
-  Parcours de formation personnalisé par étudiant
- Visibilité en temps réel sur les compétences de la promotion

## Comment ça marche
1. Les données étudiants sont collectées via formulaire et imports
2. Stockées dans **MongoDB** — base flexible adaptée aux profils variés
3. Les relations sont modélisées dans **Neo4j** , base de données graphe pour 
   les connexions entre étudiants, compétences et cours
4. Le système analyse le graphe pour faire des recommandations