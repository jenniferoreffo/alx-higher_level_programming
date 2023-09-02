#!/usr/bin/python3

"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    '''creates table state in the database
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
