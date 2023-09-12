#!/usr/bin/python3
"""
Class MyInt derives from int object
"""


class MyInt(int):
    """
    Class MyInt derives from int object

    """

    def __eq__(self, value):
        """ override the method __eq__"""
        return self.real != value

    def __ne__(self, value):
        """override method __ne__"""
        return self.real == value
