#!/usr/bin/python3

""" This script changes the name of the state object in the database htbn_0e_0_usa"""

from sys import argv                                    from model_state import Base, State
from sqlalchemy import create_engine
from Sqlalchemy.orm import sessionmaker

if __name__ == "__main__":                              

"""                                                     Access to the database and get the states
    from the database."""                                                                                           db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_ engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    ariz_state = session.query(State).filter(State.id == '2').first()
    ariz_state.name = 'New Mexico'
    session.commit()
    session.close()
        print('{0}: {1}'.format(instance.id, instance.name))
