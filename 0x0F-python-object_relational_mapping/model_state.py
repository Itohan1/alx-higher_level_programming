#!/usr/bin/python3
"""sqlalchemy declaration"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
