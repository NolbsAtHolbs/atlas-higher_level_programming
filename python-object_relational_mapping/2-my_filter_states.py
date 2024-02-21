#!/usr/bin/python3
"""Script that displays all values in states table where name matches arg"""
import MySQLdb
import sys


def match_states():
    dbconnect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                password=sys.argv[2], database=sys.argv[3])
    dbcursor = dbconnect.cursor()
    dbcursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}'"
        "ORDER BY id ASC".format(sys.argv[4]))
    rows = dbcursor.fetchall()
    for row in rows:
        print(row)
    dbcursor.close()
    dbconnect.close()


if __name__ == "__main__":
    match_states()
