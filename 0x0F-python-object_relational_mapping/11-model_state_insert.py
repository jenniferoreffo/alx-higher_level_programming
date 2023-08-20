#!/usr/bin/python3

""" Thus script adds the state object 'Louisian to the database 'htbn_0e_6_usa' 
"""
from sys import argv                                    from model_state import Base, State
from sqlalchemy import create_engine
from Sqlalchemy.orm import sessionmaker

if __name__ == "__main__":                              
"""                                                     Access to the database and get the states
    from the database."""                                                                                           db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_ engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    lou_state = State(name='Lousiana')
    session.add(lou_state)
    session.commit()                                        print('{0}'.format(lou_state.id))
    session.close()
