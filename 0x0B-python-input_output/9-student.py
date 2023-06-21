#!/usr/bin/python3
"""This module define a class student"""
class student:
"""Represents a student"""
    def __init__(self, first_name, last_name, age):
"""Initialize a new student"""
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    def to_json(self):
"""Gets a dictionary representation of the student"""
    return self.__dict__

