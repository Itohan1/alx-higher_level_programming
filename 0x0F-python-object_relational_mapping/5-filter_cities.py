#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def con_injection(user, passwd, db):
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db,
        charset="utf8"
    )

    cur = conn.cursor()

    query = """SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC"""

    search = arg[4]

    cur.execute((query), (search,))

    rows = cur.fetchall()

    v = [value[0] for value in rows]
    print(", ".join(v))

    cur.close()
    conn.close()


if __name__ == '__main__':
    arg = sys.argv
    con_injection(arg[1], arg[2], arg[3])
