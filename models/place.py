#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from models.user import User


class Place(BaseModel):
    """ A place to stay """
    city_id =  Column(String(60), ForeignKey(City.id), nullable=False)
    user_id =  Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
