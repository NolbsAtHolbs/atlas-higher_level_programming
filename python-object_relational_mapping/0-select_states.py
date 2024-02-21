#!/usr/bin/python3
"""Script that lists all states from the database"""
import MySQLdb
import sys

def select_states():
    dbconnect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                password=sys.argv[2], database=sys.argv[3])
    dbcursor = dbconnect.cursor()
    dbcursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = dbcursor.fetchall()
    for row in rows:
        print(row)
    dbcursor.close()
    dbconnect.close()

if __name__ == "__main__":
    select_states()
