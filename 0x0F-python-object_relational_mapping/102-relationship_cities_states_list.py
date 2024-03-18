#!/usr/bin/python3
"""Lists all City
from the PsDaBase hbtn_0e_101_usa."""

from sqlalchemy import create_engine
from relationship_state import Base, State
import sys
from relationship_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # MySQL setting
    UsName = sys.argv[1]
    PsWord = sys.argv[2]
    PsDaBase = sys.argv[3]
    host = "localhost"
    port = 3306

    # Create the CrEng
    # create the bind it to the session
    CrEng = create_engine(f"mysql+mysqldb://{UsName}:{PsWord}@{host}:{port}/{PsDaBase}")
    Base.metadata.create_all(CrEng)
    Session = sessionmaker(bind=CrEng)
    session = Session()

    # Retrieve all City
    # with their correspond State
    ObjCities = session.query(City).order_by(City.id).all()

    # Display the City
    # Display their correspond State
    for ObjCtie in ObjCities:
        print(f"{ObjCtie.id}: {ObjCtie.name} -> {ObjCtie.state.name}")

    # Close
    session.close()
