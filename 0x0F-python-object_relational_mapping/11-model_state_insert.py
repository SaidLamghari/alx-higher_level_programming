#!/usr/bin/python3
"""Adds the object 'Louisiana'
to the PsDaBase hbtn_0e_6_usa"""
from sqlalchemy import create_engine

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

    # Create the Engine
    # bind it to the session
    CrEngine = create_engine(f"mysql+mysqldb://{UsName}:\
                           {PsWord}@{host}:{port}/{PsDaBase}")
    Session = sessionmaker(bind=CrEngine)
    session = Session()

    # Create a new ObjState
    nObjState = State(name="Louisiana")

    # Add the new
    session.add(nObjState)
    session.flush()

    # Commit the session
    session.commit()

    # Print
    print(nObjState.id)

    # Close
    session.close()
