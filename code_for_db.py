import sqlite3

connect = sqlite3.connect("Building_in_date")
cursor = connect.cursor()

d = dates.dates
mas = d.keys()
for i in range(len(d.keys())):
    cursor.execute(f"""INSERT INTO Dates (years, months, days) values ({mas[i][2]}, {mas[i][1]}, {mas[i][0]})""")
    l = d[mas[i]]
    for t in range(l.size()):
        for j in range(l[t].size()):
            cursor.execute(f"""INSERT INTO Windows (Light, Room, Floor, IDdate) 
            values ({l[t][j][1]}, {l[t][j][0]}, {t + 1}, {i})""")
