#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from os import getenv

class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @hybrid_property
        def cities(self):
            """A getter attribute cities that returns
            the list of City instances with state_id
            equals to the current State.id => It
            will be the FileStorage relationship
            between State and City"""
            from .city import City
            from __init__ import storage
            related_cities = []
            list_of_cities = storage.all(City)
            for city in list_of_cities:
                if 'state_id' in city.keys():
                    if State.id == city['state_id']:
                        related_cities.append[city]
            return related_cities

    cities = relationship("City", back_populates="state", lazy="dynamic")
