#!/usr/bin/python3
"""
Displays the values
in the states table
of hbtn_0e_0_usa
where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # MySQL setting
    UsName = sys.argv[1]
    PsWord = sys.argv[2]
    DaBase = sys.argv[3]
    SatName = sys.argv[4]
    host = "localhost"
    port = 3306

    # Connect to the server of MySQL
    db = MySQLdb.connect(
        host=host, port=port,
        user=UsName,
        passwd=PsWord,
        db=DaBase
    )

    # Create a ObjCursor to execute SQL
    ObjCursor = db.cursor()

    # The SQL to select states with the name that is provided
    SqlQry = "SELECT * FROM states WHERE name LIKE BINARY '{}'"
    ObjCursor.execute(SqlQry.format(SatName))

    # Return the QuRows
    QuRows = ObjCursor.fetchall()

    # Print
    for PrRow in QuRows:
        print(PrRow)

    # Close the connection of DaBase and the ObjCursor
    ObjCursor.close()

    db.close()
