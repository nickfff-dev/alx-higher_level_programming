#!/usr/bin/python3
"""this module is a test that defines a class
    for the unittest of class Rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """Defines a class for the unittest of class Rectangle"""

    @classmethod
    def setUpClass(cls):
        """This method will be called once at the beginning of the test"""
        cls.rect1 = Rectangle(10, 2)
        cls.rect2 = Rectangle(2, 10)
        cls.rect3 = Rectangle(10, 2, 0, 0, 12)

    def test_instance(self):
        """Test if the instances correctly inherits from Base"""
        self.assertIsInstance(self.rect1, Base)
        self.assertIsInstance(self.rect2, Base)
        self.assertIsInstance(self.rect3, Base)

    def test_attrs(self):
        """Test verifies the assignment of attributes"""
        self.assertEqual(self.rect1.width, 10)
        self.assertEqual(self.rect1.height, 2)
        self.assertEqual(self.rect1.x, 0)  # should take default value
        self.assertEqual(self.rect1.y, 0)  # should take default value
        self.assertEqual(self.rect2.width, 2)
        self.assertEqual(self.rect2.height, 10)
        self.assertEqual(self.rect2.x, 0)
        self.assertEqual(self.rect2.y, 0)
        self.assertEqual(self.rect3.width, 10)
        self.assertEqual(self.rect3.height, 2)
        self.assertEqual(self.rect3.x, 0)
        self.assertEqual(self.rect3.y, 0)

    def test_id(self):
        """Test verifies if id is correctly assigned"""
        # No id is provided, so it should take the default increment value

        self.assertEqual(self.rect1.id, 5)

        # An id is provided, so it should take the provided value
        self.assertEqual(self.rect2.id, 6)

        # An id is provided, so it should take the provided value
        self.assertEqual(self.rect3.id, 12)

    def test_docstrings(self):
        """Test if docstrings are present"""
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)
