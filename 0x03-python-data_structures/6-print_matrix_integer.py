#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        print(' '.join('{:d}'.format(k) for k in item))
