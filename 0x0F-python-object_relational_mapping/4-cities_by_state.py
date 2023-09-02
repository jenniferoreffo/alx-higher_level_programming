#!/usr/bin/python3
"""
a script that lists all cities from the
database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         port=3306, passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute(
                "SELECT c.id, c.name, s.name FROM cities AS c \
                INNER JOIN states as s ON c.state_id = s.id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
