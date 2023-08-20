#!/usr/bin/python3

""" This prints all city objects from the db htbn_0e_0_usa"""

from sys import argv                                    from model_state import Base, State
from sqlalchemy import create_engine
from Sqlalchemy.orm import sessionmaker

if __name__ == "__main__":                              
"""                                                     Access to the database and get the cities from the database."""
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_ engine(db_uri)
    Session = sessionmaker(bind=engine)                                                                             session = Session()
    query = session.query(City, State).join(State)

    for _c, _s in query.all():
        print('{}: ({d:}) {}'.format(_s.name, _c.id, _c.name))
    session.commit()
    session.close()
