import mysql.connector

cnx = mysql.connector.connect(
    user='root', 
    password='123',
    host='localhost',
    database='movies'
)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def template_test():
    cursor = cnx.cursor()
    sql = "SELECT * FROM judul"
    cursor.execute(sql)
    data = cursor.fetchall()
    return render_template('template.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)