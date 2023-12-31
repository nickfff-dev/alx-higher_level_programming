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

    @property
    def size(self):
        """ Getter for size which represents the width of
            the square as a square's width and height are equal."""
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size.

            Note:
            It uses the setters for width and height from
            the Rectangle class for validation.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update the square attributes. """
        attrs = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for attr, arg in zip(attrs, args):
                if attr == "size":
                    self.width = arg
                    self.height = arg
                else:
                    setattr(self, attr, arg)
        else:
            if len(kwargs):
                for key in kwargs:
                    if key == "size":
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    elif key in attrs:
                        setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
