#!/usr/bin/python3
"""Write a script that prints the first State object"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
            """mysql+mysqldb://{}:{}@localhost/{}"""
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_a = (
            session.query(State).filter(State.name.like('%a%'))
            .order_by(State.id).all()
            )

    if state_a:
        for states in state_a:
            print('{}: {}'.format(states.id, states.name))
    session.close()
