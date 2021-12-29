import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    password="password",
    port="3306",
    user="root"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

mydb2 = mysql.connector.connect(
    host="127.0.0.1",
    password="password",
    port="3306",
    user="root",
    database="mydatabase"
)

mycursor2 = mydb2.cursor()
mycursor2.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

mydb.commit()
