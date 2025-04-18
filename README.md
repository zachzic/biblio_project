# 📚 Projet Django – Application de Gestion de Bibliothèque

Bienvenue dans *Ma Bibliothèque*, une application Django permettant de gérer l'inventaire de livres, les emprunts par les utilisateurs, et les retours. Ce projet a été réalisé dans le cadre d’un exercice de fin de formation afin de mettre en pratique mes compétences en développement web avec Django.

---

## 🚀 Fonctionnalités

- Affichage de la liste des livres disponibles
- Authentification des utilisateurs (login/logout)
- Emprunt de livres (limite de 3 emprunts en cours par utilisateur)
- Retour de livres avec mise à jour automatique du stock
- Gestion des rôles :
  - **Administrateur** : peut créer/modifier les livres, auteurs, catégories via l’interface d’administration Django
  - **Utilisateur** : peut uniquement emprunter et retourner ses propres livres
- Feedback utilisateur via des messages visuels (succès, erreur, etc.)
- Séparation des vues publiques et protégées (connexion requise pour voir les emprunts)

---

## 🛠️ Stack technique

- **Backend** : Django 3.2 / Python 3.11
- **Base de données** : SQLite
- **Authentification** : système intégré de Django
- **Frontend** : HTML, Bootstrap 5

---

## 📸 Capture d’écran

> Ajouter une capture ici si possible : liste des livres + interface d’emprunts.

---

## ⚙️ Installation (en local)

### Prérequis

- Python 3.10 ou supérieur
- pip / venv

### Étapes

```bash
# Cloner le projet
git clone https://github.com/votre-utilisateur/biblio_projet.git
cd biblio_projet

# Créer et activer un environnement virtuel
python -m venv venv
source venv/bin/activate  # sous Windows : venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
