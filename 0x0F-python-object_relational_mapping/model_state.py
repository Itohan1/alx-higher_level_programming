#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys

Base = declarative_base()

class State(Base):
    __tablename__ = 'hbtn_0e_6_usa'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "", sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    for states in session.query(State).order_by(State.id).all():
    print("{}: {}".format(states.id, states.name))

    session.close()
