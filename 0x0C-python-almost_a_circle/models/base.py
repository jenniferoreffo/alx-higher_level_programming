#!/usr/bin/python3
""" Defines a Base Model Class """

class Base:
    
    """ Represents the Base model
    Attributes:
        __nb_objects (int): The number of instantiated Bases."""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize a new Base
        Args: int d: identity
        """
        if id is not None:

            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
