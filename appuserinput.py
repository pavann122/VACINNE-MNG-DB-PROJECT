//user input approach -Prompt the user for their MySQL credentials at runtime:

import mysql.connector

host = input("Enter MySQL host: ")
user = input("Enter MySQL username: ")
password = input("Enter MySQL password: ")
database = input("Enter MySQL database name: ")

db_config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database
}

# Connect to the database
connection = mysql.connector.connect(**db_config)

# Your application logic here

connection.close()
