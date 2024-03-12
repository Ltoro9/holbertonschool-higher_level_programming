#!/usr/bin/python3
"""
    script that takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa
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
    cursor.execute("SELECT cities.name FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    WHERE states.name = BINARY %s", (sys.argv[4],))

    rows = cursor.fetchall()

    total_rows = len(rows)

    for row in range(total_rows):
        print(rows[row][0], end="")
        if row < total_rows - 1:
            print(", ", end="")
    print()


    cursor.close()
    db.close()
