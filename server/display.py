import pygal
import sqlite3
# radar_chart = pygal.Radar()
# radar_chart.title = 'V8 benchmark results'
# radar_chart.x_labels = ['cpu', 'cores', 'ram']
# radar_chart.add('158.1.234.1', [23, 1, 12])
# radar_chart.add('158.133.232.54', [50, 1, 14])
# radar_chart.add('157.122.534.143', [70, 2, 16])
# radar_chart.render()
# radar_chart.render_to_file('bar_chart.svg')
#

db = sqlite3.connect('flux.db')

cursor = db.cursor()

cursor.execute("""SELECT ip,cpu,cores,ram,disk,memory FROM machines""")
rows = cursor.fetchall()
for row in cursor:
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
