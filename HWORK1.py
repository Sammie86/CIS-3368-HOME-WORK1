import mysql.connector

db = mysql.connector.connect(
        host="locahost",
        user="root",
        passwd="root"
    )

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE testdatabase")