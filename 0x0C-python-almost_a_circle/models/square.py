#!/usr/bin/python3
"""
    class Square inherits class Rectangle
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
        Square inherits rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initialises Square (overrides Rectangle init)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returns Square size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets the value of size
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value
