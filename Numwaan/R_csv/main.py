import mysql.connector

#ทำการเชื่อมต่อกับฐานข้อมูล
connection = mysql.connector.connect(
 host="localhost",
 user="",
 password="",
 database="mydatabase"
)
#print(connection)
mycursor = mydb.cursor()

#create a database named "mydatabase":
mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)