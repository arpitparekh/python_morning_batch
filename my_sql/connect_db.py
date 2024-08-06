import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Walden0042$$",
  database="authentication"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name,price FROM product")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)