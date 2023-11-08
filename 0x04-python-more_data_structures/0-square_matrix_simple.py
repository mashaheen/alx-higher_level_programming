#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_list = [[x**2 for x in r] for r in matrix]
    return n_list
