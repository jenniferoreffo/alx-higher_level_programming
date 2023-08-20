#!/usr/bin/python3
"""
This script prints all city objects from the db htbn_0e_0_usa"""

from sys import argv
from relationship_city import city
from relationship_state import Base, State
from sqlalchemy import create_engine
from Sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

"""                                                     Access to the database and get the cities from the database."""

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    
    engine = create_ engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)                                                                             session = Session()                                     cal_state = State(name='California')
    sfr_city = City(name='San Francisco')
    cal_state.cities.append(sfr_city)

    session.add(cal_state)
    session.commit()
    session.close()
