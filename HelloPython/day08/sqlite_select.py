import sqlite3

conn = sqlite3.connect('myDB.db')

cursor = conn.cursor() #커서 생성

sql = "select col01, col02, col03 from mytable"
cursor.execute(sql)

for row in cursor :
    print(row[0],row[1],row[2])

cursor.close()
conn.close()
