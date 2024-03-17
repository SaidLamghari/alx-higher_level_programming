#!/usr/bin/python3
"""Changes the name of object
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

    # Create the CrEngn
    # bind it to the session
    CrEngn = create_engine(f"mysql+mysqldb://{UsName}:\
                           {PsWord}@{host}:{port}/{PsDaBase}")

    Session = sessionmaker(bind=CrEngn)

    session = Session()

    # Retrieve the object with id = 2
    ObjState = session.query(State).filter(State.id == 2).first()

    # Change the name to "New Mexico"
    if ObjState is not None:
        ObjState.name = "New Mexico"
        session.commit()

    # Close
    session.close()
