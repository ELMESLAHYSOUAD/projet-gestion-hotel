USE hotel_db;
-- Table Hotel
CREATE TABLE Hotel (
    id INT PRIMARY KEY,
    ville VARCHAR(50),
    pays VARCHAR(50),
    code_postal INT
);
-- Table Client
CREATE TABLE Client (
    id INT PRIMARY KEY,
    adresse VARCHAR(100),
    ville VARCHAR(50),
    code_postal INT,
    email VARCHAR(100),
    telephone VARCHAR(20),
    nom VARCHAR(50)
);
-- Table Prestation
CREATE TABLE Prestation (
    id INT PRIMARY KEY,
    prix INT,
    nom VARCHAR(50)
);

-- Table TypeChambre
CREATE TABLE TypeChambre (
    id INT PRIMARY KEY,
    libelle VARCHAR(50),
    prix INT
);

-- Table Chambre
CREATE TABLE Chambre (
    id INT PRIMARY KEY,
    numero INT,
    etage INT,
    balcon BOOLEAN,
    id_hotel INT,
    id_type_chambre INT,
    FOREIGN KEY (id_hotel) REFERENCES Hotel(id),
    FOREIGN KEY (id_type_chambre) REFERENCES TypeChambre(id)
);
-- Table Reservation
CREATE TABLE Reservation (
    id INT PRIMARY KEY,
    date_debut DATE,
    date_fin DATE,
    id_client INT,
    id_chambre INT,
    FOREIGN KEY (id_client) REFERENCES Client(id),
    FOREIGN KEY (id_chambre) REFERENCES Chambre(id)
);

-- Table Evaluation
CREATE TABLE Evaluation (
    id INT PRIMARY KEY,
    date_evaluation DATE,
    note INT,
    commentaire TEXT,
    id_client INT,
    FOREIGN KEY (id_client) REFERENCES Client(id)
);

