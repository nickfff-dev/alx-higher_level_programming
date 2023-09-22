#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect

"""This module Defines a class for the unittest of class Base
"""


class test_base(unittest.TestCase):
    """
        Defines a class for the unittest of class Base.
    """
    def test_id_none(self):
        """
            Test with no id
        """
        testnbase = Base()
        self.assertEqual(1, testnbase.id)

    def test_id(self):
        """
            Test with a valid id
        """
        testnbase = Base(50)
        self.assertEqual(50, testnbase.id)

    def test_id_zero(self):
        """
            Test with an id 0
        """
        testnbase = Base(0)
        self.assertEqual(0, testnbase.id)

    def test_id_negative(self):
        """
            Test with a negative id
        """
        testnbase = Base(-20)
        self.assertEqual(-20, testnbase.id)

    def test_id_string(self):
        """
            Test with an id that is not an int
        """
        testnbase = Base("Betty")
        self.assertEqual("Betty", testnbase.id)

    def test_id_list(self):
        """
            Test with an id that is not an int
        """
        testnbase = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], testnbase.id)

    def test_id_dict(self):
        """
            Test with an id that is not an int
        """
        testnbase = Base({"id": 109})
        self.assertEqual({"id": 109}, testnbase.id)

    def test_id_tuple(self):
        """
            Test with an id that is not an int
        """
        testnbase = Base((8,))
        self.assertEqual((8,), testnbase.id)

    def test_to_json_type(self):
        """
            Testing the json string
        """
        testnsquare = Square(1)
        json_dict = testnsquare.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        """
            Testing the json string
        """
        testnsquare = Square(1, 0, 0, 609)
        json_dict = testnsquare.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        """
            Testing the json string
        """
        testnsquare = Square(1, 0, 0, 609)
        json_dict = testnsquare.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        """
            Testing the json string
        """
        testnsquare = Square(1, 0, 0, 609)
        json_dict = testnsquare.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


class TestSquare(unittest.TestCase):
    """
    class for testing Base class" methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
