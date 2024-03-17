#!/usr/bin/python3
"""create the State class
initializes an instance of Base"""
import sys

from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

# Create instance
Base = declarative_base()


class State(Base):
    """
    Rep state
    table in the database
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
