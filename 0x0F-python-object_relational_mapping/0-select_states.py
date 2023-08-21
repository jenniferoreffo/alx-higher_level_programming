#!/usr/bin/python3

""" A script that lists all states from the db 'hbtn_0e_0_usa' """

if __name__ == '__ main__'

import MySQLdb
from sys import argv

""" Access to the db and get the states fron the db """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwrd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute('SELECT id, name  FROM states ORDER BY id;')

    rows = cur.fetchall()
    for row in rows:
        print(f"{rows}")
    cur.close()
    db.close()
