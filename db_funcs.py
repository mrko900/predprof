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

def get_all_days():
    connect = sqlite3.connect("db.sqlite3")
    cursor = connect.cursor
    a = cursor.execute("select count(*) from dates").fetchall()[0]
    res = {}
    for i in range(a):
        k = cursor.execute("select count(distinct floor) from windows").fetchall()[0]
        sp = []
        for j in range(k):
            mas = cursor.execute(f"""SELECT light, room from windows where IDdate = {i} and floor = {j + 1}""").fetchall()
            sp.append(mas)
        res[i] = sp

def get_one_days(day, month, year):
    connect = sqlite3.connect("db.sqlite3")
    cursor = connect.cursor
    a = cursor.execute(f"select id from dates where year = {year} and month = {month} and day = {day}").fetchall()[0]
    res = []
    k = cursor.execute(f"select count(distinct floor) from windows where IDdate = {a}").fetchall()[0]
    for j in range(k):
        mas = cursor.execute(f"""SELECT light, room from windows where IDdate = {a} and floor = {j + 1}""").fetchall()
        res.append(mas)
    res[i] = sp

