#!/bin/bash
"""Module inherits from mylist"""


class MyList(list):
    """ A class that inherits from list called MyList """
    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self))
