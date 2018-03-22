import psutil
file = open("config.txt", "a")
file.write(psutil.cpu_count(logical=False))
file.close()
