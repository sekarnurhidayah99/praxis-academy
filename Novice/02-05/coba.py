#!/usr/bin/python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='123', database='employees')
cursor = mariadb_connection.cursor()

