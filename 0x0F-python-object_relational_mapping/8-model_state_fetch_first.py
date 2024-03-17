#!/usr/bin/python3
"""Prints the first object
from the PsDaBase hbtn_0e_6_usa."""
import sys

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from model_state import Base, State

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

    # Retrieve the first object
    # from the PsDaBase
    frState = session.query(State).order_by(State.id).first()

    # Print first object
    if frState is None:
        print("Nothing")
    else:
        print(f"{frState.id}: {frState.name}")

    # Close
    session.close()
