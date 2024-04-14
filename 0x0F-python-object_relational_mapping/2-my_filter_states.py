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
    curr.execute(
        """SELECT * FROM {}.states
        WHERE states.name = "{}"
        ORDER BY states.id ASC"""
        .format(sys.argv[3], sys.argv[4])
    )
    q_rows = curr.fetchall()

    for rows in q_rows:
        print(rows)

    curr.close()
    conn.close()
