import sqlite3
import algorithms


def push_to_db():
    connect = sqlite3.connect("db.sqlite3")
    cursor = connect.cursor()
    d = algorithms.dates.dates
    i = 0
    for entry in d.keys():
        cursor.execute(f"""INSERT INTO Dates (Year, Month, Day) values ({entry[2]}, {entry[1]}, {entry[0]})""")
        l = d[entry]
        for t in range(len(l.data)):
            for j in range(len(l.data[t])):
                cursor.execute(f"""INSERT INTO Windows (Light, Room, Floor, IDdate) 
                values ({l.data[t][j][1]}, {l.data[t][j][0]}, {t + 1}, {i})""")
        i += 1
    connect.commit()

