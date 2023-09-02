#!/usr/bin/python3
'''select specific column in database'''

if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], password=argv[2],
                         db=argv[3], host='localhost',
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT id, name FROM states
            WHERE name = BINARY '{}' ORDER BY id;""".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(f"{row}")
    cur.close()
    db.close()
