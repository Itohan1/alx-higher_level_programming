#!/usr/bin/python3
"""Write a python file that contains the class definition"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import registry
import sys

Base = declarative_base()


class State(Base):
    """Write a python file that contains the class definition"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="parent")

