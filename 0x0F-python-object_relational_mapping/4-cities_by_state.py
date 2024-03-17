#!/usr/bin/python3
"""
Lists all cities
from DaBase hbtn_0e_4_usa
"""

import sys

import MySQLdb

if __name__ == "__main__":
    # MySQL setting
    UsName = sys.argv[1]
    PsWord = sys.argv[2]
    DaBase = sys.argv[3]
    host = "localhost"
    port = 3306

    # Connect to the server of MySQL
    db = MySQLdb.connect(
        host=host,
        port=port, user=UsName,
        passwd=PsWord,
        db=DaBase
    )

    # Create a ObjCursor to execute SQL
    ObjCursor = db.cursor()

    # The SQL to select all cities
    # states's corresponding
    QuRows = "SELECT cities.id, cities.name, states.name FROM cities \
             JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    ObjCursor.execute(QuRows)

    # Return the QuRows
    QuRows = ObjCursor.fetchall()

    # Print
    for PrRow in QuRows:
        print(PrRow)

    # Close the connection of DaBase and the ObjCursor
    ObjCursor.close()

    db.close()
