#!/usr/bin/python3
"""
Displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument
(safe from SQL injection)
"""

import sys

import MySQLdb


def escape_string(value):
    """
    Escapes special characters in a string
    to prevent SQL injection
    """
    db = MySQLdb.connect()
    EscpdVal = db.escape_string(value)
    db.close()
    return EscpdVal


if __name__ == "__main__":
    # MySQL setting
    UsName = sys.argv[1]
    PsWord = sys.argv[2]
    DaBase = sys.argv[3]
    SatName = escape_string(sys.argv[4])
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

    # The SQL to select states with the name that is provided
    SqlQry = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    ObjCursor.execute(SqlQry, (SatName,))

    # Return the QuRows
    QuRows = ObjCursor.fetchall()

    # Print
    for PrRow in QuRows:
        print(PrRow)

    # Close the connection of DaBase and the ObjCursor
    ObjCursor.close()

    db.close()
