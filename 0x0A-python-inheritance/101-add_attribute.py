#!/usr/bin/python3
""" defines a function that adds attributes """


def add_attribute(obj, attri, value):
    """ Adds new attribute to an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("cant add new attribute")
    setattr(obj, attri, value)
