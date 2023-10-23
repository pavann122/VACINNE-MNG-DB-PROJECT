import mysql.connector as sql
#create table in database
def crdb():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql')
    mycur=mydb.cursor()
    mycur.execute('create database if not exists Vaccine')
    print('database created')
#to show tables in datbase
def showdb():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql')
    mycur=mydb.cursor()
    mycur.execute('show databases')
    for i in mycur:
        print(i)
    mydb.close()
#create table in database
def  createtb():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
    mycur=mydb.cursor()
    mycur.execute('create table if not exists vaccine_management(name varchar(20),Aadhar_number int,Vaccine_type varchar(15),age int)')
    print("table created")
    mydb.close()
#show tables
def showtb():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
    mycur=mydb.cursor()
    mycur.execute('show tables')
    data=mycur.fetchall()
    for i in data:
        print(i)
    mydb.close()
#to know the structures of data
def desc():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
    mycur=mydb.cursor()
    mycur.execute('desc vaccine_management')
    for g in mycur:
        print(g)
    mydb.close()
#to insert values in table
def insert():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
    mycur=mydb.cursor()
    count=int(input("enter number of person to get vaccinated"))
    for i in range(count):
        name =input("enter name of person")
        adhr_num=int(input("enter adhar number"))
        vt=input("type of vaccine")
        age=int(input("enter your age"))
        data=("insert into vaccine_management values('{}',{},'{}',{})").format(name,adhr_num,vt,age)
    print('\n\nData is sucessfully added!!\n')
    mydb.commit()
    mydb.close()
#to display all record
def displaytb():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
    mycur=mydb.cursor()
    mycur.execute('select*from vaccine_management')
    data=mycur.fetchall()
    for i in data:
        print(i)
    mydb.close()
#to search an record
def search():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
    mycur=mydb.cursor()
    adr=int(input("enter adhar no to be searched"))
    s=("select*from vaccine_management where Aadhar_number={}").format(adr)
    mycur.execute(s)
    data=mycur.fetchone()
    print(data)
    mydb.close()
#to update any data
def update():
        mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
        mycur=mydb.cursor()
        adr=int(input('enter Aadhar_number to be updated'))
        n=input('\nenter new name of the person')
        vt=input('enter type of the vaccine')
        age=int(input("enter your age"))
        mycur.execute("update vaccine_management set name='{}',Aadhar_number={},vaccine_type='{}',age={}".format(n,vt,age,adr))
        mydb.commit()
        print('\n\nData is succefully Updated\n')
        mydb.close()
#to delete record from the table
def delete():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
    mycur=mydb.cursor()
    adhr_num=int(input("enter adhar number to delete a record"))
    mycur.execute("delete from vaccine_management where Aadhar_number='{}'".format(adhr_num))
    mydb.commit()
    print('deleted succesfully')
    mydb.close()
#to add a column
def Alteradd():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
    mycur=mydb.cursor()
    mycur.execute("alter table vaccine_management add column contact int")
    print('\n\ncolumn added successfully\n')
    mydb.close()
#to modify the table
def primary():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',databse='Vaccine')
    mycur=mydb.cursor()
    mycur.execute("alter table vaccine_management add primarykey(adhar_number)")
    print('\ncolumn adhar number is now a primary key\n')
    myb.close()
#to drop a column
def dropcolumn():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
    mycur=mydb.cursor()
    d=input("enter column name u want ot delete")
    mycur.execute("alter table vaccine_management drop{}".format(d))
    print('\ncolumn',d,'dropped succesfully')
    mydb.close()
#to arrange in order of aadhar number
def orderby():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
    mycur=mydb.cursor()
    mycur.execute('select*from vaccine_management order by adhar_number')
    for i in mycur:
        print(i)
    mydb.close()
#to grup by Vaccine type
def groupby():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
    mycur=mydb.cursor()
    mycur.execute('select*from vaccine_management group by vaccine_type')
    data=mycur.fetchall()
    for x in data:
        print(x)
    mydb.close()
def count():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
    mycur=mydb.cursor()
    mycur.execute('select count(*)from vaccine_management')
    data=mycur.fetchall()
    for x in data:
        print(x)
#to delete the system
def dropdb():
    mydb=sql.connect(host='localhost',user='pawan',password='mysql',database='Vaccine')
    mycur=mydb.cursor()
    mycur.execute('drop database vaccine')
    print("\n\nDatabase dropped succesfully\n")
    mydb.close()


#Main menu
while True:
    print('<>'*30)
    print('\t\t\t WELCOME VACCINATION MANAGEMENT PROGRAM')
    print('<>'*30)
    print('~'*50)
    print('press1 to create database')
    print('press2 to display databases')
    print('press3 to create table')
    print('press4 to show tables in database')
    print('press5 to display structure of table')
    print('press6 to insert data')
    print('press7 to display data')
    print('press8 to search a record stored')
    print('press9 to update a record')
    print('press10 to delete a record')
    print('press11 to add a column')
    print('press12 to add a primary key')
    print('press13 to drop a column')
    print('press14 to order by adhar number')
    print('press15 to group by Vaccinetype')
    print('press16 to count all the entries')
    print('press17 to drop database')
    print('press18 to exit')
    print('~'*50)
    ch=int(input("enter your choice"))
    if ch==1:
        crdb()
    elif ch==2:
        showdb()
    elif ch==3:
        createtb()
    elif ch==4:
        showtb()
    elif ch==5:
        desc()
    elif ch==6:
        insert()
    elif ch==7:
        displaytb()
    elif ch==8:
        search()
    elif ch==9:
        update()
    elif ch==10:
        delete()
    elif ch==11:
        Alteradd()
    elif ch==12:
        primary()
    elif ch==13:
        dropcolumn()
    elif ch==14:
        orderby()
    elif ch==15:
        groupby()
    elif ch==16:
        count()
    elif ch==17:
        dropdb()
    elif ch==18:
        print('thankyou\n stay safe and healthy')
        break
    else:
        print('wrong choice')
        
    
        
    
