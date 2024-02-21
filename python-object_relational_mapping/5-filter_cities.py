#!/usr/bin/python3
"""Script that lists all cities from the database by taking a state arg"""
import MySQLdb
import sys


def cities_in_state():
    dbconnect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                password=sys.argv[2], database=sys.argv[3])
    dbcursor = dbconnect.cursor()
    SQLcommand = ("SELECT cities.name FROM cities \
                  JOIN states ON cities.state_id = states.id \
                  WHERE states.name = %s \
                  ORDER BY cities.id ASC")
    dbcursor.execute(SQLcommand, (sys.argv[4],))
    rows = dbcursor.fetchall()
    for row in rows:
        print(row)
    dbcursor.close()
    dbconnect.close()


if __name__ == "__main__":
    cities_in_state()
