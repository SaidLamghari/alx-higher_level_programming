#!/usr/bin/python3
"""
Lists states from
the DaBase hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # MySQL connection
    UsName = sys.argv[1]
    PsWord = sys.argv[2]
    DaBase = sys.argv[3]
    host = "localhost"
    port = 3306

    # Connect to the MySQL
    db = MySQLdb.connect(
        host=host, port=port,
        user=UsName, passwd=PsWord,
        db=DaBase
    )

    # Create a ObjCursor to execute SQL
    ObjCursor = db.cursor()

    # The SQL to select states
    ObjCursor.execute("SELECT * FROM states ORDER BY id ASC")

    # The rows returned
    QuRows = ObjCursor.fetchall()

    # Print
    for PrRow in QuRows:
        print(PrRow)

    # Close the ObjCursor and DaBase
    ObjCursor.close()
    db.close()
