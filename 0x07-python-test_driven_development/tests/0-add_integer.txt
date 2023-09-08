Test cases for 0-add_integer module
===================================

The 0-add_integer module returns the sum of two numbers int or float

Usage
=====

importing function:
    >>> add_integer = __import__('0-add_integer').add_integer

two positive ints
    >>> add_integer(13, 14)
    27

one positive and one negative integer
    >>> add_integer(13, -43)
    -30

two negative ints
    >>> add_integer(-60, -65)
    -125

an integer number and a string
    >>> add_integer(41, "Nickson")
    Traceback (most recent call last):
	      ...
    TypeError: b must be an integer

a float and a string
    >>> add_integer(13.5, "Nickson")
    Traceback (most recent call last):
	      ...
    TypeError: b must be an integer

Passing no argument to the function
    >>> add_integer()
    Traceback (most recent call last):
	      ...
    TypeError: a must be an integer

string and  number
    >>> add_integer('r', 20)
    Traceback (most recent call last):
              ...
    TypeError: a must be an integer


two float numbers
    >>> add_integer(9.2, 10.2)
    19.4
