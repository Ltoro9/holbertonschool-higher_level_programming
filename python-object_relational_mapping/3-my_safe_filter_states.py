#!/usr/bin/python3
"""
    write a script that takes in arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument. But
    this time, write one that is safe from MySQL injections!
"""


import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = BINARY %s\
                    ORDER BY id ASC", (sys.argv[4],))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
