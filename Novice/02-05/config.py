import mysql.connector

config = {
  'user': 'root',
  'password': '123',
  'host': 'localhost',
  'database': 'movies',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()
print(cnx)