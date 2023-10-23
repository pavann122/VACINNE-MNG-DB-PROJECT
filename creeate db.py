import mysql.connector as sql
mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='hello')
mycur=mydb.cursor()
mycur.execute("select * from bookno")
data=mycur.fetchall()
for i in data:
    print(i)
