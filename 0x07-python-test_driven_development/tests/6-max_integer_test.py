#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Defines a class for testing the function max_integer
    """

    def test_list_of_integers(self):
        """
        Test a list of positive integers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """
        Test an empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_list_of_one_integer(self):
        """
        Test a list with a single integer
        """
        self.assertEqual(max_integer([5]), 5)

    def test_list_of_negative_integers(self):
        """
        Test a list of negative integers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_with_same_integers(self):
        """
        Test a list with identical integers
        """
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_non_integer_in_list(self):
        """
        Test a list with a non-integer element
        """

        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', 4])


if __name__ == '__main__':
    unittest.main()
