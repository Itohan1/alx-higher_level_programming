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

    state_id = (
            session.query(State).filter(State.name == sys.argv[4])
            .order_by(State.id).first()
            )

    if state_id:
        print(state_id.id)
    else:
        print("Not found")
    session.close()
