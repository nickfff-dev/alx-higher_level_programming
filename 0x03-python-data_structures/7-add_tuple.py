#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    lena = len(tuple_a)
    lenb = len(tuple_b)
    if lena > 1 and lenb > 1:
        res_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
        return res_tuple
    else:
        if lena == 0 and lenb == 0:
            res_tuple = 0, 0
            return res_tuple
        if lena == 1 and lenb == 1:
            res_tuple = tuple_a[0] + tuple_b[0], 0
            return res_tuple
        elif lena == 0 and lenb > 1:
            res_tuple = tuple_b[0], tuple_b[1]
            return res_tuple
        elif lena == 0 and lenb == 1:
            res_tuple = tuple_b[0], 0
            return res_tuple
        elif lena == 1 and lenb > 1:
            res_tuple = tuple_a[0] + tuple_b[0], tuple_b[1]
            return res_tuple
        elif lena > 1 and lenb == 0:
            res_tuple = tuple_a[0], tuple_a[1]
            return res_tuple
        elif lena > 1 and lenb == 1:
            res_tuple = tuple_a[0] + tuple_b[0], tuple_a[1]
            return res_tuple
        elif lena == 1 and lenb == 0:
            res_tuple = tuple_a[0], 0
