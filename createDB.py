import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="toor"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE crud")
