#!/usr/bin/python3
""" inherits from the BaseGeometry class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ class defines rectangle """

    def __init__(self, width, height):
        """ Initializing New Rectangle with BaseGeometry """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """ str function for rectangle

        Returns:
        Return width/height
        """
        return '[Rectangle]' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """ implements area method  """
        return self.__width * self.__height
