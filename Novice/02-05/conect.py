import mysql.connector

cnx = mysql.connector.connect(
    user='root', 
    password='123',
    host='localhost',
    database='movies'
    )


if cnx.is_connected():
    print("Berhasil terhubung ke db")
