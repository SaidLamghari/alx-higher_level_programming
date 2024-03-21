#!/usr/bin/python3
# Def. the class  State
# Autor : SAID LAMGHARI

from sqlalchemy import Column, Integer, String
from relationship_city import Base, City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(Base):
    """
    Represents a State.
    Attributes:
        __tablename__ : The database table name.
        id : The primary key.
        cities : The relationship between State and City. name : The name.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade="all, delete", backref="state")
