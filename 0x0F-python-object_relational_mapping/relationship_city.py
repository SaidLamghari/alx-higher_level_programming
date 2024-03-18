#!/usr/bin/python3
"""
Defines the class City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey

from relationship_state import Base

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship


class City(Base):
    """
    Represents a City.

    Attributes:
        __tablename__ (str): The database table name.

        id : The primary key .

        state_id : The foreign key .

        name : The name column.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
