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
        instance method that retrieves attributes in dictionary
        rep of instance
        Returns:
            attribute in _dict_ that are included in attrs
        """

        if attrs:
            array = list(map(lambda key: (key, self.__dict__[key])
                             if key in self.__dict__ else None, attrs))
            array = [i for i in array if i is not None]
            return dict(array)
        else:
            return self.__dict__
