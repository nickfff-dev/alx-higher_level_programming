#!/usr/bin/python3
"""
This script defines a City class that inherits
from a Base class to work with MySQLAlchemy ORM.
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    defines a class for the entity cities

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The city id of the class
        name (str): The city name of the class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    state = relationship('State', back_populates='cities')


State.cities = relationship('City', order_by=City.id,
                            back_populates='state')
