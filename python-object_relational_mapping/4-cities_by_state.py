#!/usr/bin/python3
"""Script that displays all values in states table where name matches arg,
and is safe from SQL injection"""
import MySQLdb
import sys


def match_states_safe():
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
    match_states_safe()
