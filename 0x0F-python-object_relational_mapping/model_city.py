#!/usr/bin/python3
'''creates cities tables'''
from sqlalchemy import String, Integer, Column, ForeignKey
from model_state import Base


class City(Base):
    '''creates a class for cities table'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'))
