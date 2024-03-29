#!/usr/bin/python3

"""This is a module for a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """This is a function that divides all elements of a matrix"""
    if not (all(isinstance(row, list) for row in matrix)
            or not all(all(isinstance(element, (int, float))
                for element in row) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
