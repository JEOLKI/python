import sqlite3

conn = sqlite3.connect('myDB.db')

cursor = conn.cursor()

sql = "select col01, col02, col03 from mytable"

cursor.execute(sql)
rows = cursor.fetchall()

for row in rows :
    print(row[0],row[1],row[2])

conn.close()
