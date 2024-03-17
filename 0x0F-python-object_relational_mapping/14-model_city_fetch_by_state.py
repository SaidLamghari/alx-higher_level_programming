#!/usr/bin/python3
"""Prints all City objects from the PsDaBase hbtn_0e_14_usa."""
from sqlalchemy import create_engine

from model_city import City

import sys

from model_state import Base, State

from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # MySQL setting
    UsName = sys.argv[1]
    PsWord = sys.argv[2]
    PsDaBase = sys.argv[3]
    host = "localhost"
    port = 3306

    # Create the CrEngn
    # bind it to the session
    CrEngn = create_engine(f"mysql+mysqldb://{UsName}:\
                           {PsWord}@{host}:{port}/{PsDaBase}")
    Session = sessionmaker(bind=CrEngn)
    session = Session()

    # Retrieve objects
    # from the PsDaBase
    ObjCities = session.query(City).order_by(City.id).all()

    # Print
    for PrCity in ObjCities:
        StName = (session.query(State.name).filter(State.id == PrCity.state_id).scalar())
        print(f"{StName}: ({PrCity.id}) {PrCity.name}")

    # Close
    session.close()
