from flask import Flask, render_template,request
import mysql.connector as mariadb

app = Flask(__name__)

@app.route('/')
def list():
    conn = mariadb.connect(user='root', password='123', database='movies')

    cur=conn.cursor()
    cur.execute("SELECT * FROM detail")
    rows=cur.fetchall()
    return render_template("hello.html",rows=rows)

if __name__=='main':
    app.run(debug = True)