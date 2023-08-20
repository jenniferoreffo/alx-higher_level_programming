#!/usr/bin/python3
"""Create states table in hbtn_0e_0_usa with some data"""
import MYSQLbd
from sys import argv

if __name__ == '__main__':
""" Access the db and get the states from there"""
    db = MSQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states \ WHERE name LIKE BINARY '{}' \ ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)

