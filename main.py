import mysql.connector
from mysql.connector.cursor import MySQLCursor

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Zealsam86!",
    database="shoppinglist"
)
mycursor = db.cursor()
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)





    
