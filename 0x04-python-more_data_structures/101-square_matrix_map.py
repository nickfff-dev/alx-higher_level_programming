#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if len(matrix) == 0:
        return matrix
    else:
        sq_matrix = \
            list(map(lambda x: list(map(lambda y: y ** 2, x)), matrix))
        return sq_matrix
