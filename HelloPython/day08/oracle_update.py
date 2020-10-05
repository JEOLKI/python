import cx_Oracle

conn = cx_Oracle.connect("HJG/java@localhost:1521/xe")
cursor = conn.cursor() #커서생성

sql="update pytable set col02=:1, col03=:2 where col01=:3"

data=(4,4,3)

cursor.execute(sql,data)
cursor.close()
conn.commit()
conn.close()

