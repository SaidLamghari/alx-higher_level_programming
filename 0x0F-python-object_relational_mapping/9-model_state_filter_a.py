#!/usr/bin/python3
"""Lists all objects
that contain the letter 'a'
from the PsDaBase hbtn_0e_6_usa"""
import sys

from sqlalchemy import create_engine

from model_state import Base, State

from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # MySQL setting
    UsName = sys.argv[1]
    PsWord = sys.argv[2]
    PsDaBase = sys.argv[3]
    host = "localhost"
    port = 3306

    # Create the engine
    # bind it to the session
    engine = create_engine(f"mysql+mysqldb://{UsName}:\
            {PsWord}@{host}:{port}/{PsDaBase}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all objects
    # containing the letter 'a'
    # sort them by ID
    ObjStates = session.query(State)
    .filter(State.name.like('%a%')).order_by(State.id).all()

    # The print
    for ObjState in ObjStates:
        print(f"{ObjState.id}: {ObjState.name}")

    # Close
    session.close()
