#!/usr/bin/python3

"""
This script prints the first state object from the database 'htbn_0e_6_usa'
"""
from sys import argv                                    from model_state import Base, State
from sqlalchemy import create_engine
from Sqlalchemy.orm import sessionmaker

if __name__ == "__main__":                              

"""                                                     Access to the database and get the state from the database."""
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_ engine(db_uri)
    Session = sessionmaker(bind=engine)                                                                             session = Session()                                     instance = session.query(State).order_by(State.id).first()

    if instance is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(instance.id, instance.name))
