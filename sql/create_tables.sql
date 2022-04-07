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

CREATE TABLE IF NOT EXISTS comments
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    id_character integer,
    id_episode integer,
    air_date date,
    comment character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT comments_pkey PRIMARY KEY (id),
    CONSTRAINT fk_comments_id_character FOREIGN KEY (id_character)
        REFERENCES public.characters (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        NOT VALID,
    CONSTRAINT fk_comments_id_episode FOREIGN KEY (id_episode)
        REFERENCES public.episodes (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        NOT VALID
);
