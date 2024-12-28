# JO
devoir du bloc 3 / dev python


tickets/
├── models.py        # Modèles de données
├── views/
│   ├── __init__.py  # Rendre le dossier un package Python
│   ├── base_views.py       # Vues génériques ou de base
│   ├── offer_views.py      # Vues pour gérer les offres
│   ├── order_views.py      # Vues pour gérer les commandes
│   ├── ticket_views.py     # Vues pour les e-tickets
├── services/
│   ├── __init__.py  # Rendre le dossier un package Python
│   ├── qr_code.py   # Génération des QR codes
│   ├── security.py  # Fonctions liées à la sécurité (clefs, hachage, etc.)
│   ├── payments.py  # Mock de gestion des paiements
│   ├── email.py     # Envoi d'e-mails
├── urls.py          # URL de l'application
├── templates/       # Fichiers HTML
│   ├── tickets/
│       ├── base.html        # Template de base
│       ├── offer_list.html  # Liste des offres
│       ├── order_confirm.html # Confirmation commande
