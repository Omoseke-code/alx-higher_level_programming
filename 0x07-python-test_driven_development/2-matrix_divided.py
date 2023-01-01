#!/usr/bin/python3
"""Dividing a 2x2 matrix"""


def matrix_divided(matrix, div):
    """returns a newly divided matrix
    Args:
        matrix (list): a list of list
        div (int): divisor
    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        ZeroDivisionError: division by zero
        TypeError: div must be a number
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
