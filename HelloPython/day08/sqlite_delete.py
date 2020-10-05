import sqlite3

conn = sqlite3.connect('myDB.db')

cursor = conn.cursor() #커서생성

sql = "delete from mytable where col01=:1"

data=('2')

cursor.execute(sql,data)
cursor.close()
conn.commit()
conn.close()