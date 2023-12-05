#!/usr/bin/python3
""" This module defines a function that finds peak in unsorted array"""


def find_peak(list_of_integers, start=0, end=None):
    """Find a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    if end is None:
        end = len(list_of_integers) - 1

    if start == end:
        return list_of_integers[start]

    mid = (start + end) // 2
    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers, mid + 1, end)
    else:
        return find_peak(list_of_integers, start, mid)
