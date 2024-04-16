#!/usr/bin/python3
"""Write a python file that contains the class definition"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import registry
import sys
from model_state import Base


class City(Base):
    """Write a python file that contains the class definition"""
    __tablename__ = 'cities'
    id = Column(
            Integer, unique=True,
            nullable=False, autoincrement=True,
            primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    parent = relationship("State", back_populates="cities")
