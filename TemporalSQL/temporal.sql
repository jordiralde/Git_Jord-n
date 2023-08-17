
/*		Esto es un comentario de multi-lineas
	-- Esto es un comentario de una linea
		NO IMPORTAN LAS MAYUSCULAS AL MOMENTO DE HACER UNA BASE DE DATOS
*/

-- CREATE DATABASE MiBD;
SHOW DATABASES;
USE mibd;

/*			CREATE TABLE
CREATE TABLE usu(
	id INT AUTO_INCREMENT,
    usuario VARCHAR(255)NOT NULL,
    contraseña VARCHAR(255)NOT NULL,
    PRIMARY KEY (id)
);
*/

/*			INSERT
INSERT INTO Usu (usuario, contraseña) VALUES ('Jordan', 'jordanjuega');
INSERT INTO Usu (usuario, contraseña) VALUES ('Jordyn', 'pepeortiva');
INSERT INTO Usu (usuario, contraseña) VALUES ('Jordon', 'pepe');
*/

/*			ALTER TABLE		PARA MODIFICAR UNA TABLA
ALTER TABLE Usu MODIFY COLUMN id INT AUTO_INCREMENT;
 	Esto va a cambiar una columna (id) para que sea autoincrementado
*/
-- # Table	Create Table
CREATE TABLE `usu` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(255) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
);
INSERT INTO usu (usuario, contraseña) VALUES ('Jordan', 'jordanjuega');
INSERT INTO usu (usuario, contraseña) VALUES ('MATE', 'pepeortiva');
INSERT INTO usu (usuario, contraseña) VALUES ('SEBA', 'pepe');

SHOW CREATE TABLE usu;
SELECT * FROM usu;
SELECT * FROM usu WHERE id = 1;
SELECT * FROM usu WHERE  usuario = 'MATE' AND contraseña = 'pepeortiva';

UPDATE usu SET contraseña = 'pepe' WHERE id = 2;

DELETE FROM usu WHERE id= 3;