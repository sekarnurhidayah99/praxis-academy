import mysql.connector

cnx = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd ='123',
    database ='kuliah'
)

cursor = cnx.cursor()
sql = """ CREATE TABLE mahasiswas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nim varchar(10),
    nama varchar(35),
    alamat varchar(50)
)
"""
cursor = cnx.cursor()
sql = "INSERT INTO mahasiswas (nim, nama, alamat) VALUES (%s, %s, %s)"
values = [
    ("170001601", "sekarnur", "jogja"),
    ("170001602", "nurhidayah", "jakarta"),
    ("170001603", "cintiakus", "cilacap")
]

for val in values:
    cursor.execute(sql, val)

cursor = cnx.cursor()
sql = "SELECT * FROM mahasiswas"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)
