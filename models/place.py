#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.orm import backref, relationship
from models.base_model import BaseModel
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import FLOAT, Float, Integer, String
from models.base_model import Base, BaseModel
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    # reviews = relationship('Review', backref='place',
    #                        cascade=('all, delete'))
