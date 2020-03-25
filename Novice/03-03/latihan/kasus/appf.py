from flask import Flask, render_template, request
import mysql.connector as mariadb

app = Flask(__name__)

@app.route("/")
def list():
    con = mariadb.connect(
        host="localhost",
        user="root",
        password="123",
        database='movies'
    )
    cur=con.cursor()
    cur.execute("SELECT * FROM detail")
    rows=cur.fetchall()
    return render_template("data.html", rows=rows)

if __name__==('__main__'):
    app.run(debug=True)