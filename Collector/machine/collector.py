# -*- coding: utf-8 -*-
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
    return res

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
    response = "OS: %s\nVersion: %s" % (os, version)
    response += "\nName: %s\nNB_CPU: %s" % (name, cores)
    response += "\nDisk: %s%%" % disk_percent
    response += "\nCPU: %s" % getCPU()
    response += "Memory: %s%%" % memory_percent
    response += "\nSince: %s" % running_since
    response += "\nRAM: %s%%\n" % getRAM()
    return response


hote = "159.89.17.141"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print "Connection on {}".format(port)

socket.send(getInfo())

print "Close the connection"
socket.close()
