import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",passwd="Zealsam86!")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM shoppinglist.`cis shoppinglist")

for i in mycursor:
    print(i)