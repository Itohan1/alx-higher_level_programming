#!/usr/bin/python3
"""Write a script that prints the first State object"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from sqlalchemy.orm import registry

if __name__ == '__main__':

    engine = create_engine(
            """mysql+mysqldb://{}:{}@localhost/{}"""
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    a = session.query(City).order_by(City.id).all()
    for b in a:
        print('{}: ({}) {}'.format(b.parent.name, b.id, b.name))
    session.close()
