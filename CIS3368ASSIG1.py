import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Zealsam86!",
    database="shoppinglist"
)
mycursor = db.cursor()

print("shoppinglist")

shoplist =[]

add = input("want to add something to your shopping list? Y or N?")

while add.lower() == "Y":
    item = input ("Enter your item to the list:")
    shoplist.append(item)
    add = input ("want to add to your shopping list? Y or N?")

    print()
    print ("Here is your alphabetized shopping list.")
    shoplist.sort()
    for listitem in shoplist:
        print(listitem)

