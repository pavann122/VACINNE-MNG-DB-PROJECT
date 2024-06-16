import configparser
import mysql.connector as sql

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

db_config = {
    'host': config['mysql']['host'],
    'user': config['mysql']['user'],
    'password': config['mysql']['password'],
    'database': config['mysql']['database']
}

def crdb():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    mycur.execute('CREATE DATABASE IF NOT EXISTS Vaccine')
    print('Database created')
    mydb.close()

def showdb():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    mycur.execute('SHOW DATABASES')
    for i in mycur:
        print(i)
    mydb.close()

def createtb():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    mycur.execute('CREATE TABLE IF NOT EXISTS vaccine_management(name VARCHAR(20), Aadhar_number INT, Vaccine_type VARCHAR(15), age INT)')
    print("Table created")
    mydb.close()

def showtb():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    mycur.execute('SHOW TABLES')
    data = mycur.fetchall()
    for i in data:
        print(i)
    mydb.close()

def desc():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    mycur.execute('DESC vaccine_management')
    for g in mycur:
        print(g)
    mydb.close()

def insert():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    count = int(input("Enter number of persons to get vaccinated: "))
    for i in range(count):
        name = input("Enter name of person: ")
        adhr_num = int(input("Enter Aadhar number: "))
        vt = input("Type of vaccine: ")
        age = int(input("Enter your age: "))
        data = "INSERT INTO vaccine_management VALUES('{}', {}, '{}', {})".format(name, adhr_num, vt, age)
        mycur.execute(data)
        print('\n\nData is successfully added!\n')
    mydb.commit()
    mydb.close()

def displaytb():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    mycur.execute('SELECT * FROM vaccine_management')
    data = mycur.fetchall()
    for i in data:
        print(i)
    mydb.close()

def search():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    adr = int(input("Enter Aadhar number to be searched: "))
    s = "SELECT * FROM vaccine_management WHERE Aadhar_number = {}".format(adr)
    mycur.execute(s)
    data = mycur.fetchone()
    print(data)
    mydb.close()

def update():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    adr = int(input('Enter Aadhar_number to be updated: '))
    n = input('\nEnter new name of the person: ')
    vt = input('Enter type of the vaccine: ')
    age = int(input("Enter your age: "))
    mycur.execute("UPDATE vaccine_management SET name='{}', vaccine_type='{}', age={} WHERE Aadhar_number={}".format(n, vt, age, adr))
    mydb.commit()
    print('\n\nData is successfully updated\n')
    mydb.close()

def delete():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    adhr_num = int(input("Enter Aadhar number to delete a record: "))
    mycur.execute("DELETE FROM vaccine_management WHERE Aadhar_number = {}".format(adhr_num))
    mydb.commit()
    print('Deleted successfully')
    mydb.close()

def Alteradd():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    mycur.execute("ALTER TABLE vaccine_management ADD COLUMN contact INT")
    print('\n\nColumn added successfully\n')
    mydb.close()

def primary():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    mycur.execute("ALTER TABLE vaccine_management ADD PRIMARY KEY (Aadhar_number)")
    print('\nColumn Aadhar_number is now a primary key\n')
    mydb.close()

def dropcolumn():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    d = input("Enter column name you want to delete: ")
    mycur.execute("ALTER TABLE vaccine_management DROP {}".format(d))
    print('\nColumn', d, 'dropped successfully')
    mydb.close()

def orderby():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    mycur.execute('SELECT * FROM vaccine_management ORDER BY Aadhar_number')
    for i in mycur:
        print(i)
    mydb.close()

def groupby():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    mycur.execute('SELECT * FROM vaccine_management GROUP BY Vaccine_type')
    data = mycur.fetchall()
    for x in data:
        print(x)
    mydb.close()

def count():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    mycur.execute('SELECT COUNT(*) FROM vaccine_management')
    data = mycur.fetchall()
    for x in data:
        print(x)
    mydb.close()

def dropdb():
    mydb = sql.connect(**db_config)
    mycur = mydb.cursor()
    mycur.execute('DROP DATABASE Vaccine')
    print("\n\nDatabase dropped successfully\n")
    mydb.close()

while True:
    print('<>'*30)
    print('\t\t\t WELCOME VACCINATION MANAGEMENT PROGRAM')
    print('<>'*30)
    print('~'*50)
    print('Press 1 to create database')
    print('Press 2 to display databases')
    print('Press 3 to create table')
    print('Press 4 to show tables in database')
    print('Press 5 to display structure of table')
    print('Press 6 to insert data')
    print('Press 7 to display data')
    print('Press 8 to search a record stored')
    print('Press 9 to update a record')
    print('Press 10 to delete a record')
    print('Press 11 to add a column')
    print('Press 12 to add a primary key')
    print('Press 13 to drop a column')
    print('Press 14 to order by Aadhar number')
    print('Press 15 to group by Vaccine type')
    print('Press 16 to count all the entries')
    print('Press 17 to drop database')
    print('Press 18 to exit')
    print('~'*50)
    ch = int(input("Enter your choice: "))
    if ch == 1:
        crdb()
    elif ch == 2:
        showdb()
    elif ch == 3:
        createtb()
    elif ch == 4:
        showtb()
    elif ch == 5:
        desc()
    elif ch == 6:
        insert()
    elif ch == 7:
        displaytb()
    elif ch == 8:
        search()
    elif ch == 9:
        update()
    elif ch == 10:
        delete()
    elif ch == 11:
        Alteradd()
    elif ch == 12:
        primary()
    elif ch == 13:
        dropcolumn()
    elif ch == 14:
        orderby()
    elif ch == 15:
        groupby()
    elif ch == 16:
        count()
    elif ch == 17:
        dropdb()
    elif ch == 18:
        print('Thank you\nStay safe and healthy')
        break
    else:
        print('Wrong choice')
