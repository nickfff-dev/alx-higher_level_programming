#!/usr/bin/python3

"""
Class MyList that inherits from list.
"""


class MyList(list):
    """
    Class MyList that inherits from list.

    Methods:
        print_sorted: Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Method to print the list in ascending order.
        """
        print(sorted(self))
