===========================
How to Use 4-print_square.py
===========================

This module defines a ``print_square(size)`` function.

Usage
=====

::

    >>> print_square = __import__('4-print_square').print_square
    >>> print_square(3)
    ###
    ###
    ###

::

    >>> print_square(1)
    #
	
Invalid Sizes
===============

The parameter ``size`` must be a non-negative integer. Otherwise, a TypeError or ValueError is raised.

::

    >>> print_square(-5)
    Traceback (most recent call last):
    ValueError: size must be >= 0

::

    >>> print_square("four")
    Traceback (most recent call last):
    TypeError: size must be an integer

::

    >>> print_square(1.5)
    TypeError: size must be an integer
