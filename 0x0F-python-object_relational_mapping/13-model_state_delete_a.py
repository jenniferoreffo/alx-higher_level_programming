#!/usr/bin/python3

""" This script deletes all thr state objects with a name containing the letter 'a' from the database 'htbn_0e_0_usa'"""

from sys import argv                                    from model_state import Base, State
from sqlalchemy import create_engine
from Sqlalchemy.orm import sessionmaker

if __name__ == "__main__":                              
"""Deletes staye objects on the database."""

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_ engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    for instance in session.query(State).filter(State.name.contains('a')):
    session.delete(instance)

    session.commit()
    session.close()
        print('{0}: {1}'.format(instance.id, instance.name))
