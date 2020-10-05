import cx_Oracle

conn = cx_Oracle.connect("HJG/java@localhost:1521/xe")
cursor = conn.cursor() #커서생성

sql = "delete from pytable where col01=:1"

data=('3')

cursor.execute(sql,data)
cursor.close()
conn.commit()
conn.close()