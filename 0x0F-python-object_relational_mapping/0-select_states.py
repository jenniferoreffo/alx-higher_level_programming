#!/usr/bin/python3
""" A script that lists all states from the db 'hbtn_0e_0_usa' """

import MySQLdb
from sys import argv

if __name__ == '__ main__' 
""" Access to the db and get the states fron the db """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwrd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(rows)
