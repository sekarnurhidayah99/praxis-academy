import mysql.connector

cnx = mysql.connector.connect(user='root', password='123',
                              host='localhost',
                              database='movies')
cnx.close()

print(cnx)