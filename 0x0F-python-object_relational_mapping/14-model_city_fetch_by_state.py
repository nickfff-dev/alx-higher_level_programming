#!/usr/bin/python3
"""
This module defines a script that lists all State objects
containing 'a' from a database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State.name.label('state_name'),
                             City.id, City.name.label('city_name'))\
            .join(City).order_by(City.id):
        print("{}: ({}) {}".format(row.state_name, row.id, row.city_name))
    session.close()
