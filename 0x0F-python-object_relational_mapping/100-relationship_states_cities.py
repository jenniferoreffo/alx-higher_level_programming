#!/usr/bin/python3
"""
This script prints all city objects from the db htbn_0e_0_usa"""

import sys
from relationship_city import city
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from Sqlalchemy.orm import Session

if __name__ == "__main__":

"""fetch all"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    session = Session()
    cal_state = State(name='California')
    sfr_city = City(name='San Francisco')
    cal_state.cities.append(sfr_city)

    session.add(cal_state)
    session.commit()
    session.close()
