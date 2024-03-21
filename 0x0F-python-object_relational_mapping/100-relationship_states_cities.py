#!/usr/bin/python3
"""
Module: create_california_sf

Description:
This module creates the "California" state and "San Francisco" city in the database "hbtn_0e_100_usa" using SQLAlchemy.

Author:
Said Lamghari

Dependencies:
- Pytn 3
- SQLAlchemy
- reltionship_state module
- reltionship_city module

Usage:
To use this module, you need to provide three command-line arguments: UsName, PsWord, and PsDaBase.

- UsName: The username for the database connection.
- PsWord: The password for the database connection.
- PsDaBase: The name of the database.

Note: replace "<UsName>", "<PsWord>", and "<PsDaBase>" with the actual values.
"""

from relationship_state import Base, State

import sys

from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    UsName = sys.argv[1]
    PsWord = sys.argv[2]
    PsDaBase = sys.argv[3]
    host = "localhost"
    port = 3306

    CrEng = create_engine(f"mysql+mysqldb://{UsName}:\
            {PsWord}@{host}:{port}/{PsDaBase}")

    Base.metadata.create_all(CrEng)

    Session = sessionmaker(bind=CrEng)

    session = Session()

    NwStat = State(name="California")

    NwCity = City(name="San Francisco", state=NwStat)

    session.add(NwStat)

    session.add(NwCity)

    session.commit()

    session.close()
