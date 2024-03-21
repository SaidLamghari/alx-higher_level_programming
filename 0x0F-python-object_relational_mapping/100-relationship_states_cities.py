#!/usr/bin/python3
'''
SAID LAMGHARI
'''
from relationship_state import Base, State

import sys

from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    UsName = sys.argv[1]
    PsWord = sys.argv[2]
    PsDaBase = sys.argv[3]
    host = "localhost"
    port = 3306

    CrEng = create_engine(f"mysql+mysqldb://{UsName}:\
            {PsWord}@{host}:{port}/{PsDaBase}")

    Base.metadata.create_all(CrEng)

    Session = sessionmaker(bind=CrEng)

    session = Session()

    NwStat = State(name="California")

    NwCity = City(name="San Francisco", state=NwStat)

    session.add(NwStat)

    session.add(NwCity)

    session.commit()

    session.close()
