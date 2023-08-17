#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    isEmpty = len(matrix)
    if isEmpty == 0:
        return None
    else:
        squares = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
        return squares
