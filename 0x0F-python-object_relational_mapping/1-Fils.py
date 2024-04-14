#!/usr/bin/python3
"""Write a script that takes in an argument and displays all values"""

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
            f"""SELECT * FROM states 
            WHERE BINARY states.name LIKE 'N%'
            ORDER BY states.id ASC"""
    )
    rows = curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    conn.close()
