#!/usr/bin/python3
'''fetches all rows'''
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = Session(engine)

    for result in session.query(State, City).\
            join(City, State.id == City.state_id).all():
        print("{}: ({}) {}".format(result[0].name,
                                   result[1].id, result[1].name))

    session.close()	
