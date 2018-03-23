# -*- coding: utf-8 -*-
import json
import psutil
import platform
import datetime
import subprocess
import socket

def getCPU():
    subprocess.call(["sh", "cpu.sh"])
    fichier = open("data.txt", "r")
    res = fichier.read()
    fichier.close()
    subprocess.call(["rm", "data.txt"])
    return res[:-3]

def getRAM():
    bashCommand = "free | awk 'FNR == 3 {print $3/($3+$4)*100}'"
    output = subprocess.check_output(['bash','-c', bashCommand])
    return output.rstrip()

def getInfo():
    os, name, version, _, _, _ = platform.uname()
    version = version.split('-')[0]
    cores = psutil.cpu_count()
    memory_percent = psutil.virtual_memory()[2]
    disk_percent = psutil.disk_usage('/')[3]
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    running_since = boot_time.strftime("%A %d. %B %Y")

    return json.dumps({"os":os,"v":version,"name":name,"cores":cores,"disk":disk_percent,"cpu":getCPU(),"memory":memory_percent,"ram":getRAM(),"date":running_since})



hote = "159.89.17.141"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print "Connection on {}".format(port)
socket.send(getInfo().encode())

print "Close the connection"
socket.close()
