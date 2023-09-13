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

    def to_json(self):
        """
        instance method that retrieves a dictionary rep of instance
        Returns:
            a dictionary representation of the class obj instance
        """
        return self.__dict__
