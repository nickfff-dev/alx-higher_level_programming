#!/usr/bin/python3
""" This module defines a script that uses
    mysqlclient to make queries to a db
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(password=sys.argv[2], database=sys.argv[3],
                         user=sys.argv[1], port=3306, host='localhost')
    cur = db.cursor()
    cur.execute('SELECT c.name FROM \
                states s JOIN cities c ON s.id = c.state_id \
                WHERE s.name = BINARY %(name)s\
                ORDER BY c.id ASC', {'name': sys.argv[4]})
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
