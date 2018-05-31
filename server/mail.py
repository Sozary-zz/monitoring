#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def mail(): # Permet d'envoyer un mail de crise à l'adresse mentionnée ci-dessous
    msg = MIMEMultipart()
    msg['From'] = 'chrismehdi69@gmail.com'
    msg['To'] = 'chrismehdi69@gmail.com'
    msg['Subject'] = 'Crise'
    message = 'Une situation de crise a été détectée sur votre système !'
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('chrismehdi69@gmail.com', 'bof.....')
    mailserver.sendmail('chrismehdi69@gmail.com', 'chrismehdi69@gmail.com', msg.as_string())
    mailserver.quit()
