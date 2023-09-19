#!/usr/bin/python3
"""this module defines a Base class"""
import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves object to file in CSV format"""
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as csvfile:
            if list_objs is not None and len(list_objs):
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
            else:
                csvfile.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """loads object from file in CSV format"""
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                list_objs = csv.DictReader(csvfile, fieldnames=field_names)
                if list_objs:
                    list_objs = [dict([k, int(v)] for k, v in insta.items())
                                 for insta in list_objs]
                    return [cls.create(**y) for y in list_objs]
                else:
                    return []
        except IOError:
            return []
