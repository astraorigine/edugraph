//US-06:Chemin de compétences
MATCH p = (c1:Competence {nom:"Python"})-[:EST_PREREQUIS*1..]->(c2:Competence {nom:"Deep Learning"})
RETURN nodes(p);

//US-07 :Recommander des étudiants
MATCH (e:Etudiant)-[:CONNAIT]->(c:Competence {nom:"Machine Learning"})
RETURN e.nom;