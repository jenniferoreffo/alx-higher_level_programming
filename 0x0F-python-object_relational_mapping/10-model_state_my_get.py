#!/usr/bin/python3

"""
This script prints the state object id with the name passed as argumentfron the db 'htbn_0e_6_usa'
"""

from sys import argv                                    from model_state import Base, State
from sqlalchemy import create_engine
from Sqlalchemy.orm import sessionmaker

if __name__ == "__main__":                              

"""                                                     Access to the database and get the state from the database.
"""
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_ engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    instance =  session.query(State).filter(State.name == argv[4]).first()

    if instance is None:
        print('Not found')
    else:
        print('{0}'.format(instance))
