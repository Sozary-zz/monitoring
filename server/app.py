#! /usr/bin/python
# -*- coding:utf-8 -*-
import sqlite3
from pathlib import Path
from flask import Flask, render_template

def machine(cursor): # Permet de récupérer les informations de toutes les machines du parc
    cursor.execute("""SELECT id,name,version,cpu,cores,ram,disk,memory,os,ip,age FROM machines ORDER BY date DESC""")
    machines = {}
    compt = 0
    for row in cursor:
        new_list = list()
        if not row[9] in machines:
            machines[row[9]] = list()

        for i in xrange(11):
            new_list.append(row[i])

        machines[row[9]].append(new_list)

    for k,v in machines.items():
        compt+=1
    return machines

my_file = Path("flux.db")
if not my_file.is_file():
    print "There is no data recorded yet."
    exit()

db = sqlite3.connect('flux.db')

cursor = db.cursor()

app = Flask(__name__)

@app.route('/') # L'application web se lance à la racine (localhost:8080/)
def index():
    machines = machine(cursor)
    return render_template('index.html', machines=machines) # Ainsi, le variable "machines" peut être utilisée dans la page HTML index.

if __name__ == '__main__':
    app.run(port=8080) # L'application se lance sur le port 8080 (localhost:8080)
