#!/usr/bin/python3
"""Prints object Stat with the name passed
from the PsDaBase hbtn_0e_6_usa"""
from sqlalchemy import create_engine

import sys

from model_state import Base, State

from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # MySQL setting
    UsName = sys.argv[1]
    PsWord = sys.argv[2]
    PsDaBase = sys.argv[3]
    SrchName = sys.argv[4]
    host = "localhost"
    port = 3306

    # Create Engine
    # Bind it to the session
    engine = create_engine(f"mysql+mysqldb://{UsName}:\
                           {PsWord}@{host}:{port}/{PsDaBase}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the Object
    # with the specified name
    ObjState = session.query(State).filter(State.name == SrchName).first()

    # the print
    if ObjState is not None:
        print(ObjState.id)
    else:
        print("Not found")

    # Close
    session.close()
