#!/usr/bin/python3
""" This module defines a script that uses
    mysqlclient to make filter queries to a db
"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(password=sys.argv[2], database=sys.argv[3],
                         user=sys.argv[1], port=3306, host='localhost')
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states \
                WHERE name LIKE BINARY %(name)s \
                ORDER BY id ASC", {'name': sys.argv[4]})
    rows = cur.fetchall()
    for col in rows:
        print(col)
    cur.close()
    db.close()
