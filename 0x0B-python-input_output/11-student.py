#!/usr/bin/python3
""" this module defines a class Student"""


class Student:
    """
    class Student
    Attributes:
        first_name(str): first name of student
        last_name(str): last name of student
        age(int): age of the student
    """
    def __init__(self, first_name, last_name, age):
        """
        Student instance initializer
        Args:
            first_name(str): first name of student
            last_name(str): last name of student
            age(int): age of the student
        """
        if type(age) == int:
            self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """
        instance method that retrieves attributes to a dictionary
        implementation of a serialization mechanism
        the object attributes are serialized to a json (self.__dict__)
        Returns:
            attribute in _dict_ that are included in attrs
        """

        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            array = list(map(lambda key: (key, self.__dict__[key])
                             if key in self.__dict__ else None, attrs))
            array = [i for i in array if i is not None]
            return dict(array)
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        instance method that replaces its attributes from json
        implementation of a deserialization mechanism
        the json is deserialized to the object attributes

        """
        if json:
            for k, v in json.items():
                if k in self.__dict__:
                    self.__dict__[k] = v
