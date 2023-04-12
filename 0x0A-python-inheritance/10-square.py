#!/usr/bin/python3

""" Defines a Subclass """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A new Square class inherting from Rectangle
    """
    def __init__(self, size):
        """
        function of square

        Attributes:
            size (int): size of square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
