#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'users'
        # places = relationship('Place', backref="user", cascade="all, delete")
        # class attribute places represents a relationship with the class Place
        # If the User object is deleted, all linked Place objects will be
        # automatically deleted. Also,the reference from a Place object to his
        # User is named user
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        # reviews = relationship('Review', backref='user',cascade='all,delete')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
