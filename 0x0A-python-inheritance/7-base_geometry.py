#!/usr/bin/python3
""" defines a BaseGeometry class """


class BaseGeometry:
    """ represents a base geometry """

    def area(self):
        """ Method is not implemented """
        raise Exception("area(), is not implemented")

    def integer_validator(self, name, value):
        """ that validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
