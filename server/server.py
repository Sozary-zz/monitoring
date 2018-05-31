import json
import socket
import sqlite3
import sys

db = sqlite3.connect('flux.db')

cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS machines(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     version TEXT,
     cpu INTEGER,
     cores INTEGER,
     ram INTEGER,
     disk INTEGER,
     memory INTEGER,
     os TEXT,
     ip TEXT,
     age TEXT,
     date DATE
)
""")
db.commit()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 1558))

while True:
        socket.listen(5)
        client, address = socket.accept()
        print "{} sent some data".format(address[0])
        response = client.recv(255)
        if response != "":
    		data = json.loads(response.decode())
    		data['address']=address[0]
    		cursor.execute("""
                INSERT INTO machines(name,version,cpu,cores,ram,disk,memory,os,ip,age,date)
                VALUES(:name,:v,:cpu,:cores,:ram,:disk,:memory,:os,:address,:date,date('now'))
                    """, data)
                db.commit()
                cursor.execute("""
                DELETE FROM machines WHERE date<date('now')-10
                    """)
                db.commit()

print "Close"
client.close()
socket.close()
