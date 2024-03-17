#!/usr/bin/python3
"""
Lists all states
with a name starting with N (upper N)
from the DaBase hbtn_0e_0_usa
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

    # The SQL to select states that start with 'N'
    ObjCursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # return the Rows
    QuRows = ObjCursor.fetchall()

    # Print
    for PrRow in QuRows:
        print(PrRow)

    # Close the conection of DaBase and the ObjCursorv
    ObjCursor.close()
    db.close()
