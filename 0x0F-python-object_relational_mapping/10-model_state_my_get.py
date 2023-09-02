#!/usr/bin/python3
'''fetch all rows'''
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = Session(engine)

    state = session.query(State).filter_by(name=sys.argv[4]).first()

    if state:
        print("{}".format(state.id))
    else:
        print('Not found')

    session.close()
