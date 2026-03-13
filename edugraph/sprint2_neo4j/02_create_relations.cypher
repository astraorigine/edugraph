//Alice connait ses compétences
MATCH (alice:Etudiant {nom: "Alice Mbeki"})
MATCH (py:Competence {nom: "Python"})
MATCH (sql:Competence {nom: "SQL"})
MATCH (ml:Competence {nom: "Machine Learning"})
MATCH (stat:Competence {nom: "Statistiques"})
CREATE (alice)-[:CONNAIT]->(py)
CREATE (alice)-[:CONNAIT]->(sql)
CREATE (alice)-[:CONNAIT]->(ml)
CREATE (alice)-[:CONNAIT]->(stat)

//Bob connait ses compétences
MATCH (bob:Etudiant {nom: "Bob Diallo"})
MATCH (js:Competence {nom: "JavaScript"})
MATCH (docker:Competence {nom: "Docker"})
MATCH (linux:Competence {nom: "Linux"})
CREATE (bob)-[:CONNAIT]->(py)
CREATE (bob)-[:CONNAIT]->(js)
CREATE (bob)-[:CONNAIT]->(docker)
CREATE (bob)-[:CONNAIT]->(linux)

//David connait ses compétences
MATCH (david:Etudiant {nom: "David Konan"})
MATCH (dl:Competence {nom: "Deep Learning"})
CREATE (david)-[:CONNAIT]->(py)
CREATE (david)-[:CONNAIT]->(ml)
CREATE (david)-[:CONNAIT]->(dl)
CREATE (david)-[:CONNAIT]->(sql)

//Eva connait ses compétences
MATCH (eva:Etudiant {nom: "Eva Mensah"})
MATCH (crypto:Competence {nom: "Cryptographie"})
CREATE (eva)-[:CONNAIT]->(linux)
CREATE (eva)-[:CONNAIT]->(crypto)

//Etudiants suivent des cours
MATCH (alice:Etudiant {nom: "Alice Mbeki"})
MATCH (david:Etudiant {nom: "David Konan"})
MATCH (bob:Etudiant {nom: "Bob Diallo"})
MATCH (c1:Cours {titre: "Machine Learning"})
MATCH (c2:Cours {titre: "Deep Learning"})
MATCH (c3:Cours {titre: "DevOps & Cloud"})
CREATE (alice)-[:SUIT]->(c1)
CREATE (david)-[:SUIT]->(c1)
CREATE (david)-[:SUIT]->(c2)
CREATE (bob)-[:SUIT]->(c3)

//Prérequis entre compétences
MATCH (py:Competence {nom: "Python"})
MATCH (ml:Competence {nom: "Machine Learning"})
MATCH (dl:Competence {nom: "Deep Learning"})
CREATE (py)-[:EST_PREREQUIS]->(ml)
CREATE (ml)-[:EST_PREREQUIS]->(dl)