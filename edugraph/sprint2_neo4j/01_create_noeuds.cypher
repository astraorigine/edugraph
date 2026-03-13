//Etudiants
CREATE (e:Etudiant {nom: "Alice Mbeki", niveau: "M1", filiere: "Data Science"})
CREATE (e2:Etudiant {nom: "Bob Diallo", niveau: "M1", filiere: "Génie Logiciel"})
CREATE (e3:Etudiant {nom: "David Konan", niveau: "M2", filiere: "Data Science"})
CREATE (e4:Etudiant {nom: "Eva Mensah", niveau: "M1", filiere: "Cybersécurité"})

//Compétences
CREATE (c1:Competence {nom: "Python"})
CREATE (c2:Competence {nom: "SQL"})
CREATE (c3:Competence {nom: "Machine Learning"})
CREATE (c4:Competence {nom: "Deep Learning"})
CREATE (c5:Competence {nom: "Docker"})
CREATE (c6:Competence {nom: "Statistiques"})
CREATE (c7:Competence {nom: "JavaScript"})
CREATE (c8:Competence {nom: "Linux"})
CREATE (c9:Competence {nom: "Cryptographie"})
CREATE (c10:Competence {nom: "MongoDB"})

//Cours
CREATE (cours1:Cours {titre: "Machine Learning", niveau: "M1"})
CREATE (cours2:Cours {titre: "Deep Learning", niveau: "M2"})
CREATE (cours3:Cours {titre: "DevOps & Cloud", niveau: "M1"})