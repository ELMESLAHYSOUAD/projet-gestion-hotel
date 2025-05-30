# projet-gestion-hotel
Ce projet a été réalisé dans le cadre du module Bases de Données Relationnelles sous la supervision du Pr. J. ZAHIR.  
Il consiste à modéliser, manipuler et exploiter une base de données de gestion d’hôtel à l’aide de MySQL, SQLite, Python et Streamlit.

## Fonctionnalités de l'application

- Consulter la liste des réservations
- Consulter la liste des clients
- Consulter la liste des chambres disponibles pendant une période donnée
- Ajouter un client
- Ajouter une réservation
 ## Installation et utilisation

### 1. Cloner le dépôt
git clone https://github.com/ELMESLAHYSOUAD/projet-gestion-hotel.git
cd projet-gestion-hotel

### 2. Installer les dépendances Python
pip install streamlit pandas

### 3. Initialiser la base de données SQLite
python init_db.py

### 4. Lancer l’application Streamlit
streamlit run app.py

Ouvrez ensuite votre navigateur à l’adresse [http://localhost:8501](http://localhost:8501).

---

## Structure du projet

- `init_db.py` : Script de création et remplissage de la base SQLite
- `app.py` : Application web Streamlit
- `hotel.db` : Fichier de base de données SQLite (généré par `init_db.py`)
- `README.md` : Ce fichier

---

## Vidéo de démonstration

- [Lien vers la vidéo de démonstration de l’interface (Google Drive)](https://drive.google.com/file/d/1I8xCU5Z5LKDn3Tb2hnr-tQ4UWPy5mbBW/view?usp=sharing)

---

## Livrables

- **Requêtes en algèbre relationnelle** : Voir le PDF joint au projet
- **Script SQL** : Création et remplissage des tables, fourni dans le dépôt
- **Interface** : Ce dépôt GitHub + la vidéo de démonstration

---

## Différence entre SQLite et MySQL

**SQLite** est une base de données légère, embarquée, qui fonctionne sans serveur et stocke toutes les données dans un simple fichier.  
**MySQL** est un système de gestion de base de données client-serveur, plus adapté aux applications multi-utilisateurs et aux gros volumes de données.

---

## Auteur

- Nom : Souad El Meslahy
- Filière :INF-S4
- Gr:02
- N°Appogée:2022792
- Contact: s.elmeslahy6339@uca.ac.ma

---

## Liens utiles

- [Dépôt GitHub du projet](https://github.com/ELMESLAHYSOUAD/projet-gestion-hotel)
- [Vidéo de démonstration](https://drive.google.com/file/d/1I8xCU5Z5LKDn3Tb2hnr-tQ4UWPy5mbBW/view?usp=sharing)





 

