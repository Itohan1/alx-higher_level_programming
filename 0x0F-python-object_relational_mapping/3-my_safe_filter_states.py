#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    curr = conn.cursor()
    query = """SELECT * FROM states
        WHERE BINARY name = %s
        ORDER BY id ASC"""

    search = sys.argv[4]

    curr.execute(query, (search,))

    q_rows = curr.fetchall()

    for rows in q_rows:
        print(rows)

    curr.close()
    conn.close()
