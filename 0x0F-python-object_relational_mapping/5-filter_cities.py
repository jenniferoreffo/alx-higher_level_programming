#!/usr/bin/python3
"""
a script that lists all cities from the
database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    row_list = []  # initializing the list of each row

    if len(argv[4].split()) != 1 or argv[4].find(';') != -1:
        pass

    else:
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             port=3306, passwd=argv[2],
                             db=argv[3])
        cur = db.cursor()
        cur.execute(
                    "SELECT c.name FROM cities AS c \
                    INNER JOIN states as s ON c.state_id = s.id \
                    WHERE s.name = BINARY '{:s}';".format(argv[4]))
        rows = cur.fetchall()
        for row in rows:
            row_list.append(*row)  # unpack the tuple before appending
        print(', '.join(row_list))

