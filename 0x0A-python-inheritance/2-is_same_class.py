#!/usr/bin/python3
"""Checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Return true if true object is an instance
       class, else return false
    """
    return (type(obj) == a_class)
