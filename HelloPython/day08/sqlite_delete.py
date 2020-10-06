import sqlite3

#conn = sqlite3.connect('myDB.db')

# Autocommit 사용시:
conn = sqlite3.connect("myDB.db", isolation_level=None)
cursor = conn.cursor()

sql = "delete from mytable where col01=?"

cursor.execute(sql,('2'))

cursor.close()
#conn.commit()
conn.close()