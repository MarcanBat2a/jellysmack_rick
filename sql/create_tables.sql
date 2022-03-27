CREATE TABLE IF NOT EXISTS characters (
  id INT NOT NULL,
  name varchar(250) NOT NULL,
  status varchar(250),
  species varchar(250),
  type varchar(250),
  gender varchar(250),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS episodes (
  id INT NOT NULL,
  name varchar(250),
  air_date date,
  episode varchar(250),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS characters_episodes (
  id_character INT NOT NULL, 
  id_episode INT NOT NULL,
  PRIMARY KEY (id_character, id_episode),
  FOREIGN KEY(id_character) REFERENCES characters (id),
  FOREIGN KEY(id_episode) REFERENCES episodes (id)
);
