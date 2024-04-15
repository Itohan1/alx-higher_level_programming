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

    cur.execute(
        f"""SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC"""
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == '__main__':
    arg = sys.argv
    con_injection(arg[1], arg[2], arg[3])
