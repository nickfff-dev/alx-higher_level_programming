#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    isEmpty = len(matrix)
    if isEmpty == 0:
        return None
    else:
        squares = [[elem ** 2 for elem in row] for row in matrix]
        return squares
