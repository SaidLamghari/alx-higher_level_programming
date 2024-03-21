#!/usr/bin/python3
"""State"""
from sqlalchemy import Column, Integer, String
from relationship_city import Base, City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class State(Base):
    """
    Represents State.

    Attributes:
        __tablename__ (str): The database.
        id (Column): The primary key the state ID.
        name (Column): The column the state name.
        cities (relationship): The relationship State and City.

    Author:
        Said Lamghari

    Dependencies:
        - SQLAlchemy
        - relationship_city module

    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
