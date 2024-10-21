import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Sp0ng3b0b6901!',
    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE 3340data")
print('Hello data base 3340data')