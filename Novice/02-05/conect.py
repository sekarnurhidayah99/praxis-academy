import mysql.connector

cnx = mysql.connector.connect(user='root', password='123',
                              host='localhost',
                              database='employees')
cnx.close()
print(cnx)