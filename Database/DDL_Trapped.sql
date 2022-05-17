CREATE DATABASE IF NOT EXISTS Trapped;

USE Trapped;

CREATE TABLE IF NOT EXISTS Domande (
  id_D INT NOT NULL AUTO_INCREMENT,
  domanda VARCHAR(200) NOT NULL,
  risp_A VARCHAR(200) NOT NULL,
  risp_B VARCHAR(200) NOT NULL,
  risp_C VARCHAR(200) NOT NULL,
  risp_D VARCHAR(200) NOT NULL,
  risp_Corr VARCHAR(1) NOT NULL,

  PRIMARY KEY(id_D)
);

CREATE TABLE IF NOT EXISTS Partite(
	id_U INT NOT NULL AUTO_INCREMENT,
	nome_U VARCHAR(50) NOT NULL,
	vite_U INT NOT NULL,
	aiuti_U INT NOT NULL,
	punti_U INT NOT NULL,
	
	PRIMARY KEY(id_U)
);
