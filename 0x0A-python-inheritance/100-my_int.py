#!/usr/bin/python3

""" module defines a class MyInT"""


class MyInt(int):
    """ invert == and != """

    def __eq__(self, value):
        """ Override == with != """
        return self.real != value
    
    def __ne__(self, value):
        """ Override != with == """
        return self.real == value
