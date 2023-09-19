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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

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
        if (type(list_dictionaries) != list or
                not all(type(obj) == dict for obj in list_dictionaries)):
            err = ("list_dictionaries must be a list of dictionaries")
            raise TypeError(err)
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json string to file"""
        filename = cls.__name__ + ".json"

        if list_objs is not None and len(list_objs):
            list_dictionaries = [x.to_dictionary() for x in list_objs]
        else:
            list_dictionaries = []
        obj_string = cls.to_json_string(list_dictionaries)
        with open(filename, "w", encoding="utf-8") as myfile:
            myfile.write(obj_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""

        if json_string is None or json_string == "":
            return []
        if type(json_string) is not str:
            raise TypeError("json_string must be a string")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            newobj = cls(30, 30)
        else:
            newobj = cls(30)

        newobj.update(**dictionary)
        return newobj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as myfile:
                all_objs = cls.from_json_string(myfile.read())
            if all_objs and len(all_objs):
                all_instnces = [cls.create(**obj) for obj in all_objs]
                return all_instnces
            else:
                return []
        except FileNotFoundError:
            return []
