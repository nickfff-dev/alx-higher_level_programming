#!/usr/bin/python3
""" module defines class Square that
inherits from the class Rectangle."""
from .rectangle import Rectangle


class Square(Rectangle):
    """ defines class Square that inherits from the class Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor
           Args:
               size(int): width and height of the square.
               x(int): the x coordinate of the square.
               y(int): the y coordinate of the square.
           """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str representation of class"""
        return "[Square] " + "(" + str(self.id) + ") " + str(self.x) + \
            "/" + str(self.y) + " - " + str(self.width)
