#!/usr/bin/python3
"""  New class """


class MyList(list):
    """ Mylist class that inherits from list """

    def print_sorted(self):
        """ Function that prints a sorted list """
        print(sorted(self))
