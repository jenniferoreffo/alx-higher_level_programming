#!/usr/bin/python3

"""                                                     This script lists all state objects and corresponding citt object contained in the  db htbn_0e_0_100"""

from sys
from relationship_city import city                      from relationship_state import Base, State              from sqlalchemy import create_engine
from Sqlalchemy.orm import sessionmaker
                                                        if __name__ == "__main__":                              
"""                                                     Access to the database and get the cities from the database."""                                                 
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)                        
    engine = create_ engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)                                                                             session = Session()

    st = session.query(State).outerjoin(City).order_by(State.id, City.id).all()


    for state in st:
        print("{}: {}".format(state.id, state.name)
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
