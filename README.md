Projet d'administration système réalisé en BASH et Python par Mehdi Ayache et Chris Chevalier.

Adresses IP :
- Serveur : 167.99.246.167
- Client : 167.99.253.200
=> Nous utilisons "Transmit" pour travailler sur les machines serveur et cliente à distance.

I. Collecte d’information :
- server.py : Gere la création d'un serveur en python. Il s'agit simplement d'un listener attendant des connections entrante. Les nouvelles informations des clients sont gérées avec une base de donnée SqlLite
- Ce serveur est donc ammené à recevoir des informations des clients (présents sur chaque machines du parc). Ce programme communiquant avec le serveur est lancé toutes les minutes grâce à crontab (linux). Il envois donc les données au serveur.

=> Langage utilisé: Serveur: python | Client: batch/python
=> Librairies utilisées : psutil

=> Bonus: De nombreuses informations sont collectées

II. Stockage & Collecte web :

- server.py: Comme énnoncé dans la partie I, les données sont stockées dans une base de données SqlLite dès lors que le serveur reçoit des données d'un client. De même, à chaque nouvelles acquisition de données, les informations vieille de plus de 10 jours sont supprimées.
=> Langage utilisé : Python
=> Librairies utilisées : sqlite

- webParser.py : Récupère et stock les dernières alertes CERT (http://www.cert.ssi.gouv.fr/) dans un fichier texte (alert.txt).
=> Langage utilisé : Python
=> Librairies utilisées : beautifulsoup4 / urllib2 / codecs

=> Bonus: Bdd sans serveur / ajout nouvelles machine ne nécessite pas de modification du code

III. Affichage & Alerte :

- visualize.py : Petit script permettant de choisir de visionner toutes les machines du parc et de générer un svg des états d'une machine au fil du temps et son dernier état connu.
=> Langage utilisé : Python
=> Librairies utilisées : pygale

- webParser.py : C'est dans ce document que le document alert.txt est comparé avec la dernière alerte CERT. Si celles-ci sont différents, le module d'envoi de mail prend la suite.
=> Langage utilisé : Python
=> Librairies utilisées : mail.py (Cf. ci-dessous)

- mail.py : Module d'envoi de mail en cas de situation de crise.
=> Langage utilisé : Python
=> Librairies utilisées : smtplib / email

=> Bonus: Affichage couleur du svg

IV. Communication :

- app.py : Utilise la librairie jinja pour récupérer les informations des serveurs en Python et ainsi les envoyer vers une structure HTML. Affiche ainsi les performances de nos machines accompagné de graphes et d'un historique.
=> Langage utilisé : Python
=> Librairies utilisées : jinja / flask / sqlite3 / pathlib
=> Bonus: Un module d’affichage web qui reprend les informations du client CLI

Remote machine Connection :
ssh -L 8000:127.0.0.1:8080 root@167.99.246.167 -N -v -v
=> localhost:8000
Permet d'accéder au localhost de la machine distante depuis notre propre machine via l'adresse localhost:8000.
