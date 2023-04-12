#!/usr/bin/python3
""" inherits from the BaseGeometry class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ class defines rectangle """

    def __init__(self, width, height):
        """ Initializing Rectangle with BaseGeometry """
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
