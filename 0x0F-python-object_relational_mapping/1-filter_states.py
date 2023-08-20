#!/usr/bin/python3
""" A script that lists all a states in the db hbtn_0e_0_usa that states with the letter 'N' """
import  MYSQLdb 
from sys import argv
if __name__ == '__main__':
""" Get all states from the db"""
    db = MYSQLdv.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states \ WHERE name LIKE BINARU 'N%' \ ORDER BY states id ASC")
    rows = cur.fetchall()
    fow row in rows:
        print(row)  
