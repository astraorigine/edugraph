#  Architecture ─ EduGraph

## Vue globale
```
┌─────────────────────────────────────────┐
│              EduGraph                   │
│                                         │
│  ┌──────────┐     ┌──────────────────┐  │
│  │ MongoDB  │     │      Neo4j       │  │
│  │          │     │                  │  │
│  │ Profils  │◄───►│ Relations        │  │
│  │ Cours    │     │ Compétences      │  │
│  │ Filières │     │ Parcours         │  │
│  └──────────┘     └──────────────────┘  │
│        ▲                  ▲             │
│        └────────┬─────────┘             │
│                 │                       │
│            Python                       │
│         (Intégration)                   │
└─────────────────────────────────────────┘
```

## Pourquoi deux bases de données ?

### MongoDB — Les données
- Stocke les **profils complets** des étudiants
- Structure **flexible** : ce qui fait que  chaque étudiant peut avoir des champs différents
- Idéal pour les **requêtes simples** : tel que  trouver un étudiant, filtrer par niveau

### Neo4j — Les relations
- Stocke les **connexions** entre étudiants, compétences et cours
- Idéal pour les **traversées de graphe** : par exemple les chemins, recommandations
- Questions impossibles en SQL : comme *"Quel chemin pour atteindre MLOps ?"*

## Flux de données
```
1. Données collectées → MongoDB (profils)
2. Python lit MongoDB
3. Python synchronise → Neo4j (relations)
4. Neo4j répond aux requêtes de recommandation
```

## Modèle de graphe Neo4j
```
(Etudiant)-[:CONNAIT]->(Competence)
(Etudiant)-[:SUIT]->(Cours)
(Competence)-[:EST_PREREQUIS]->(Competence)
```

## Sprints de développement
| Sprint   | Contenu |

| Sprint 1 | MongoDB CRUD : insertion, requêtes, update, delete |
| Sprint 2 | Neo4j : nœuds, relations, traversée de graphe |
| Sprint 3 | Intégration Python : synchronisation MongoDB ↔ Neo4j |
| Sprint 4 | Déploiement Docker + cloud |