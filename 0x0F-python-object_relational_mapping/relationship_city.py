#!/usr/bin/python3
"""City"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class City(Base):
    """
    Represents a City.

    Attributes:
        __tablename__ (str): The name of the database.
        id (Column): The primary key the city ID.
        name (Column): The column for the city.
        state_id (Column): The foreign key column referencing the ID.

    Author:
        Said Lamghari

    Dependencies:
        - SQLAlchemy
        - relationship_state module

    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
