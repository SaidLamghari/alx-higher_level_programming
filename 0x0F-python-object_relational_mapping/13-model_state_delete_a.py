#!/usr/bin/python3
"""Deletes all State
with a name contain letter 'a'
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
    host = "localhost"
    port = 3306

    # Create the CrEngn and bind it to the session
    CrEngn = create_engine(f"mysql+mysqldb://{UsName}:\
                           {PsWord}@{host}:{port}/{PsDaBase}")

    Session = sessionmaker(bind=CrEngn)

    session = Session()

    # Names containing the letter 'a'
    statesWa = session.query(State).filter(State.name.like("%a%")).all()

    # Delete
    for stateWa in statesWa:
        session.delete(stateWa)
    session.commit()

    # Close
    session.close()
