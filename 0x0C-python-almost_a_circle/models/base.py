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
                list_dictionaries(list): list of dicts
        """
        if list_dictionaries is None:
            return "[]"
        if not len(list_dictionaries):
            return "[]"
        if isinstance(list_dictionaries, list):
            return json.dumps(list_dictionaries)
