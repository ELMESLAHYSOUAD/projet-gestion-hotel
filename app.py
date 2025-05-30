import streamlit as st
import pandas as pd
import sqlite3
from datetime import date

def get_conn():
    return sqlite3.connect('hotel.db')

st.title("Gestion d'Hôtel - Projet S4")

menu = [
    "Liste des réservations",
    "Liste des clients",
    "Chambres disponibles (période)",
    "Ajouter un client",
    "Ajouter une réservation"
]
choice = st.sidebar.selectbox("Menu", menu)

conn = get_conn()
c = conn.cursor()

if choice == "Liste des réservations":
    st.header("Toutes les réservations")
    query = """
    SELECT r.id, c.nom, ch.numero, h.ville, r.date_debut, r.date_fin
    FROM Reservation r
    JOIN Client c ON r.id_client = c.id
    JOIN Chambre ch ON r.id_chambre = ch.id
    JOIN Hotel h ON ch.id_hotel = h.id
    """
    c.execute(query)
    data = c.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Client", "Chambre", "Hôtel", "Début", "Fin"])
    st.dataframe(df)

elif choice == "Liste des clients":
    st.header("Tous les clients")
    c.execute("SELECT id, nom, adresse, ville, code_postal, email, telephone FROM Client")
    data = c.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Nom", "Adresse", "Ville", "CP", "Email", "Téléphone"])
    st.dataframe(df)

elif choice == "Chambres disponibles (période)":
    st.header("Chambres disponibles")
    date_debut = st.date_input("Date de début", value=date(2025, 6, 15))
    date_fin = st.date_input("Date de fin", value=date(2025, 6, 18))
    if st.button("Rechercher"):
        query = """
        SELECT ch.id, ch.numero, ch.etage, ch.balcon, h.ville, t.libelle
        FROM Chambre ch
        JOIN Hotel h ON ch.id_hotel = h.id
        JOIN TypeChambre t ON ch.id_type_chambre = t.id
        WHERE ch.id NOT IN (
            SELECT id_chambre FROM Reservation
            WHERE date_debut <= ? AND date_fin >= ?
        )
        """
        c.execute(query, (date_fin, date_debut))
        data = c.fetchall()
        df = pd.DataFrame(data, columns=["ID", "Numéro", "Étage", "Balcon", "Hôtel", "Type"])
        st.dataframe(df)

elif choice == "Ajouter un client":
    st.header("Ajouter un client")
    nom = st.text_input("Nom")
    adresse = st.text_input("Adresse")
    ville = st.text_input("Ville")
    code_postal = st.number_input("Code postal", step=1)
    email = st.text_input("Email")
    telephone = st.text_input("Téléphone")
    if st.button("Ajouter"):
        c.execute("INSERT INTO Client (adresse, ville, code_postal, email, telephone, nom) VALUES (?, ?, ?, ?, ?, ?)",
                  (adresse, ville, code_postal, email, telephone, nom))
        conn.commit()
        st.success("Client ajouté !")

elif choice == "Ajouter une réservation":
    st.header("Ajouter une réservation")
    c.execute("SELECT id, nom FROM Client")
    clients = c.fetchall()
    c.execute("SELECT id, numero FROM Chambre")
    chambres = c.fetchall()
    client_id = st.selectbox("Client", [f"{x[0]} - {x[1]}" for x in clients])
    chambre_id = st.selectbox("Chambre", [f"{x[0]} - {x[1]}" for x in chambres])
    date_debut = st.date_input("Date de début")
    date_fin = st.date_input("Date de fin")
    if st.button("Ajouter la réservation"):
        id_client = int(client_id.split(" - ")[0])
        id_chambre = int(chambre_id.split(" - ")[0])
        # Générer un nouvel id pour la réservation
        c.execute("SELECT MAX(id) FROM Reservation")
        max_id = c.fetchone()[0]
        new_id = (max_id or 0) + 1
        c.execute("INSERT INTO Reservation (id, date_debut, date_fin, id_client, id_chambre) VALUES (?, ?, ?, ?, ?)",
                  (new_id, date_debut, date_fin, id_client, id_chambre))
        conn.commit()
        st.success("Réservation ajoutée !")

conn.close()
