#!/usr/bin/python3
"""Lists all ObjState
from the PsDaBase hbtn_0e_6_usa"""
import sys

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == "__main__":
    # MySQL setting
    UsName = sys.argv[1]
    port = 3306

    # Create the engine
    # bind it to the session
    engine = create_engine(f"mysql+mysqldb://{UsName}:\
            {PsWord}@{host}:{port}/{PsDaBase}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve objects
    # sort them by ID
    ObjStates = session.query(State).order_by(State.id).all()


    session.close()
