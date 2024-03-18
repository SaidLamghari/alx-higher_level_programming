#!/usr/bin/python3
"""Lists all State objects
corresponding City objects
contained in the PsDaBase hbtn_0e_101_usa."""

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
    # bind it to the session
    CrEng = create_engine(f"mysql+mysqldb://{UsName}:{PsWord}@{host}:{port}/{PsDaBase}")

    Base.metadata.create_all(CrEng)

    Session = sessionmaker(bind=CrEng)

    session = Session()

    # Retrieve all State
    # whith their corresponding City
    ObjStates = session.query(State).order_by(State.id).all()

    # Display the State
    # Display their corresponding City
    for ObjState in ObjStates:
        print(f"{ObjState.id}: {ObjState.name}")
        for city in ObjState.cities:
            print(f"\t{city.id}: {city.name}")

    # Close the session
    session.close()
