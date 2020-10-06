import sqlite3

#conn = sqlite3.connect('myDB.db')

# Autocommit 사용시:
conn = sqlite3.connect("myDB.db", isolation_level=None)

cursor = conn.cursor()

sql = "insert into mytable (col01,col02,col03) values(?,?,?)"

cursor.execute(sql, ('2','2','2'))

#conn.commit()
conn.close()



