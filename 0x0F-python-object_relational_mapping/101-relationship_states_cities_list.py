#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)                        
    engine = create_ engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)                                                         session = Session()

    st = session.query(State).outerjoin(City).order_by(State.id, City.id).all()


    for state in st:
        print("{}: {}".format(state.id, state.name)
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
