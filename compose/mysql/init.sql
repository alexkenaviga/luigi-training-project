CREATE TABLE Persons (
  id int AUTO_INCREMENT,
  Last_Name varchar(255),
  First_Name varchar(255),
  Address varchar(255),
  City varchar(255),
  PRIMARY KEY (id)
);

INSERT INTO Persons (id, Last_Name, First_Name, Address, City)
VALUES (NULL, 'Amato', 'Marta', 'Via S.Pertini Nr.3', 'Pontecagnano');

INSERT INTO Persons (id, Last_Name, First_Name, Address, City)
VALUES (NULL, 'Longo', 'Alessandro', 'Via S.Pertini Nr.3', 'Pontecagnano');