#!/usr/bin/python3
"""Defines a class for the unittest of class Base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Defines a class for the unittest of class Base"""

    @classmethod
    def setUpClass(cls):
        """This method will be called once at the
        beginning of the test"""
        cls.base1 = Base()
        cls.base2 = Base()
        cls.base3 = Base()
        cls.base4 = Base(12)
        cls.base5 = Base()

    def test_id(self):
        """Test if the 'id' has been set correctly"""
        self.assertEqual(self.base1.id, 1, 'base1 id not set correctly')
        self.assertEqual(self.base2.id, 2, 'base2 id not set correctly')
        self.assertEqual(self.base3.id, 3, 'base3 id not set correctly')
        self.assertEqual(self.base4.id, 12, 'base4 id not set correctly')
        self.assertEqual(self.base5.id, 4, 'base5 id not set correctly')

    def test_docstring(self):
        """Test if docstrings are present"""
        import models.base as mb

        # Validating module docstring
        self.assertIsNotNone(mb.__doc__)

        # Validating Base class docstring
        self.assertIsNotNone(Base.__doc__)

        # Validating Base class method docstrings
        self.assertIsNotNone(Base.__init__.__doc__)
