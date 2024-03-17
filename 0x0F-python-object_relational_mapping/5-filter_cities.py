#!/usr/bin/python3
"""
Lists all cities
of a given state
from the PsDaBase hbtn_0e_4_usa
"""

import sys

import MySQLdb


def escape_string(value):
    """
    Escapes special characters
    in a string to prevent
    SQL injection
    """
    db = MySQLdb.connect()
    EscpdVal = db.escape_string(value)
    db.close()
    return EscpdVal


if __name__ == "__main__":
    # MySQL setting
    UsName = sys.argv[1]
    PsWord = sys.argv[2]
    PsDaBase = sys.argv[3]
    SatName = escape_string(sys.argv[4])
    host = "localhost"
    port = 3306

    # Connect to the server of MySQL
    db = MySQLdb.connect(
        host=host,
        port=port, user=UsName,
        passwd=PsWord,
        db=PsDaBase
    )

    # Create a ObjCursor to execute SQL
    ObjCursor = db.cursor()

    # The SQL to select cities of the state
    QuRows = "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s ORDER BY cities.id ASC"
    ObjCursor.execute(QuRows, (SatName,))

    # The first Row returned
    DtRow = ObjCursor.fetchone()

    # Print the results
    if DtRow[0] is not None:
        print(DtRow[0])

    # Close the connection of DaBase and the ObjCursor
    ObjCursor.close()

    db.close()
