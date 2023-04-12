#!/usr/bin/python3
"""checks if object is an instance of a class that inherited from it
"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of a class that inherited from
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
