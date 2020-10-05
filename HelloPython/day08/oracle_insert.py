import cx_Oracle

conn = cx_Oracle.connect("HJG/java@localhost:1521/xe")
cursor = conn.cursor() #커서생성

sql = "insert into pytable values(:1,:2,:3)"
data=('2','2','2')

cursor.execute(sql,data)

cursor.close()
conn.commit() #JDBC는 오토 커밋 python은 오토커밋이 아니다.
conn.close()



