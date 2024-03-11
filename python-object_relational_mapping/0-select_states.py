#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb


db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="0000",
    db="hbtn_0e_0_usa"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()