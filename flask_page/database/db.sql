-- Todo list
CREATE TABLE tasks(
  code SERIAL NOT NULL,
  id_category INT NULL,
  titulo VARCHAR(50) NOT NULL,
  descripcion VARCHAR(255) NOT NULL,
  PRIMARY KEY (code)
);

CREATE TABLE categories(
  id INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  description VARCHAR(200),
  PRIMARY KEY (id)
);

ALTER TABLE tasks ADD FOREIGN KEY (id_category) REFERENCES categories(id);

-- ? Foro

CREATE TABLE foro(
  id SERIAL NOT NULL,
  person VARCHAR(60) NOT NULL,
  title VARCHAR(55) NOT NULL,
  description VARCHAR(300) NOT NULL,
  PRIMARY KEY (id)
);
