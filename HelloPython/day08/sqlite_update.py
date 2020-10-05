import sqlite3

conn = sqlite3.connect('myDB.db')

cursor = conn.cursor() #커서생성

sql="update mytable set col02=:1, col03=:2 where col01=:3"

data=(4,4,3)

cursor.execute(sql,data)
cursor.close()
conn.commit()
conn.close()

