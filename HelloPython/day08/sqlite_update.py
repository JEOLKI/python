import sqlite3

#conn = sqlite3.connect('myDB.db')

# Autocommit 사용시:
conn = sqlite3.connect("myDB.db", isolation_level=None)
cursor = conn.cursor()

sql="update mytable set col02=?, col03=? where col01=?"

cursor.execute(sql, ('4','4','3'))

#conn.commit()
conn.close()

