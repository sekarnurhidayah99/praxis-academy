from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='123',
                                 host='localhost',
                                 database='movies')
cnx.close()

print(cnx)