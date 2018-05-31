import sqlite3
import pygal
from pathlib import Path

def displayMachinesName(cursor):
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
        print('[{2}] {0} (last connection {1})'.format(k,v[0][10],compt))
        compt+=1
    return machines

def getMachineByCompt(machines,compt):
    __compt = 0
    for k,v in machines.items():
        if compt == __compt:
            return machines[k]
        __compt+=1
    return "null"

def getCPUThroughTime(machine):
    res = list()
    for x in machine:
        res.append(x[3])
    return res

def getDates(machine):
    res = list()
    for i in range(len(machine)):
        res.append(machine[i][10])
    return res
def getCPUs(machine):
    res = list()
    for i in range(len(machine)):
        res.append(machine[i][3])
    return res

def getRAM(machine):
    res = list()
    for i in range(len(machine)):
        res.append(machine[i][5])
    return res

def getMemory(machine):
    res = list()
    for i in range(len(machine)):
        res.append(machine[i][7])
    return res

def getDisk(machine):
    res = list()
    for i in range(len(machine)):
        res.append(machine[i][6])
    return res

def generateSvg(machine):
    gauge = pygal.SolidGauge(inner_radius=0.70)
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    digit_formatter = lambda x: '{:.10g}'.format(x)
    gauge.title = machine[0][9]
    gauge.value_formatter = percent_formatter
    gauge.add('CPU', [{'value': machine[0][3], 'max_value': 100}])
    gauge.add('Cores', [{'value': machine[0][4], 'max_value': 4}],formatter=digit_formatter)
    gauge.add('RAM', [{'value': machine[0][5], 'max_value': 100}])
    gauge.add('Disk', [{'value': machine[0][6], 'max_value': 100}])
    gauge.add('Memory', [{'value': machine[0][7], 'max_value': 100}])
    gauge.render_to_file('chart.svg')

    line_chart = pygal.Line()
    line_chart.title = "Evolution of {0}".format(machine[0][9])

    line_chart.x_labels = getDates(machine)
    line_chart.add('CPU', getCPUs(machine))
    line_chart.add('RAM',  getRAM(machine))
    line_chart.add('Disk', getDisk(machine))
    line_chart.add('Memory', getMemory(machine))
    line_chart.render_to_file('hist.svg')

    getCPUThroughTime(machine)

my_file = Path("flux.db")
if not my_file.is_file():
    print "There is no data recorded yet."
    exit()

db = sqlite3.connect('flux.db')

cursor = db.cursor()

while 1:
    cmd = raw_input("> ")

    if cmd == "list":
        displayMachinesName(cursor)
    if cmd == "generateSvg":
        elems = displayMachinesName(cursor)
        inp = len(elems)
        while inp < 0 or inp >= len(elems):
            inp = input("Select an element between {0} and {1}: ".format(0,len(elems)-1))
        res = getMachineByCompt(elems,inp)
        if res != "null":
            generateSvg(res)
            print "Renderred successfully!"
        else:
            print "An error occured"
    if cmd == "help":
        print("- list\n- generateSvg\n- exit")
    if cmd == "exit":
        exit()
