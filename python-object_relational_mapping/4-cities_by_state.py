#!/usr/bin/python3
"""Script that lists all cities from the database"""
import MySQLdb
import sys


def cities():
    dbconnect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                password=sys.argv[2], database=sys.argv[3])
    dbcursor = dbconnect.cursor()
    SQLcommand = ("SELECT cities.id, cities.name, states.name FROM cities \
                  LEFT JOIN states ON states.id = cities.state_id \
                  ORDER BY cities.id")
    dbcursor.execute(SQLcommand)
    rows = dbcursor.fetchall()
    for row in rows:
        print(row)
    dbcursor.close()
    dbconnect.close()


if __name__ == "__main__":
    cities()
