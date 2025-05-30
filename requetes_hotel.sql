USE hotel_db;

-- a. Afficher la liste des réservations avec le nom du client et la ville de l’hôtel réservé
SELECT
    r.id AS id_reservation,
    c.nom AS nom_client,
    h.ville AS ville_hotel
FROM
    Reservation r
    JOIN Client c ON r.id_client = c.id
    JOIN Chambre ch ON r.id_chambre = ch.id
    JOIN Hotel h ON ch.id_hotel = h.id;

-- b. Afficher les clients qui habitent à Paris
SELECT *
FROM Client
WHERE ville = 'Paris';

-- c. Calculer le nombre de réservations faites par chaque client
SELECT
    c.nom AS nom_client,
    COUNT(r.id) AS nb_reservations
FROM
    Client c
    LEFT JOIN Reservation r ON c.id = r.id_client
GROUP BY
    c.nom;

-- d. Donner le nombre de chambres pour chaque type de chambre
SELECT
    t.libelle AS type_chambre,
    COUNT(ch.id) AS nb_chambres
FROM
    TypeChambre t
    JOIN Chambre ch ON t.id = ch.id_type_chambre
GROUP BY
    t.libelle;

-- e. Afficher la liste des chambres qui ne sont pas réservées pour une période donnée
-- Exemple : chambres libres entre le 2025-06-15 et le 2025-06-18
SELECT *
FROM Chambre ch
WHERE ch.id NOT IN (
    SELECT r.id_chambre
    FROM Reservation r
    WHERE r.date_debut <= '2025-06-18'
      AND r.date_fin >= '2025-06-15'
);

-- f. Qu’est-ce que SQLite, quelle différence avec MySQL ?
-- Réponse : cf. le document PDF
