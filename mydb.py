import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

# Prepare a cusrsor object
cursorObject =  database.cursor()

# Create a database
cursorObject.execute("create database django_crm")

print("Database has been created..")

