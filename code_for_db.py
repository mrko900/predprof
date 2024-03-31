import sqlite3

connect = sqlite3.connect("Building_in_date")
cursor = connect.cursor()

d = {}
mas = d.keys()
k = 1
for i in range(d.keys().size()):
    cursor.execute(f"""INSERT INTO Dates (IDdate, years, months, days) values ({i + 1}, {mas[i][2]}, {mas[i][1]}, {mas[i][0]})""")
    l = d[mas[i]]
    for t in range(l.size()):
        for j in range(l[t].size()):
            cursor.execute(f"""INSERT INTO Windows (IDwindow, Light, Room, Floor) 
            values ({k}, {l[t][j][1]}, {l[t][j][0]}, {t + 1})""")
            k += 1
