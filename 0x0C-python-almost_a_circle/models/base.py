#!/usr/bin/python3
"""this module defines a Base class"""
import json


class Base:
    """Base Class definition
        Attributes:
                nb_objects(int): count of the class instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base class instance initialization
            Args:
                id(int): an integer of
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """the JSON string representation of list_dictionaries
         Args:
            list_dictionaries(list): a list of dicts.

        Returns:
            string
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list or \
                not all(type(obj) == dict for obj in list_dictionaries):
            err = ("list_dictionaries must be a list of dictionaries")
            raise TypeError(err)
        return json.dumps(list_dictionaries)