#!/usr/bin/python3
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from Sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

"""                                                     Access to the database and get the states
    from the database."""

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_ engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    for instance in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))