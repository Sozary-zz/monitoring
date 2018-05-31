#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib2 import urlopen
import bs4 as BeautifulSoup
import sys
import codecs
from mail import mail
reload(sys)
sys.setdefaultencoding('utf-8')

# $ apt-get install python-bs4
# $ easy_install beautifulsoup4
# $ pip install beautifulsoup4

def webParser():
    html = urlopen('http://www.cert.ssi.gouv.fr/').read() # Lit le code HTML de l'URL donné
    soup = BeautifulSoup.BeautifulSoup(html)

    date = soup.find('span', class_="item-date") # Stocke la date de la dernière alerte CERT
    date = date.text

    ref = soup.find('span', class_="item-ref") # Stocke la référence de la dernière alerte CERT
    ref = ref.text

    title = soup.find('span', class_="item-title") # Stocke le titre de la dernière alerte CERT
    title = title.text

    return "Dernière alerte : " + "\n" + date + "\n" + ref + "\n" + title # Mise en page sous forme de string de l'alerte

webParser = str(webParser())
f = codecs.open("alert.txt", 'r','utf-8') # Ouverture du fichier "alert.txt" en lecture
f2 = str(f.read())
f.close()

if f2 != webParser: # Comparaison de l'alerte stocké dans le fichier texte et de la dernière alerte récupérée sur le site.
    fichier = open("alert.txt", "w")
    fichier.write(webParser) # Écris la nouvelle alerte dans le fichier texte
    fichier.close()
    mail() # Envoi un mail d'alerte
