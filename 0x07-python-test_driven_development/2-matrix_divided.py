#!usr/bin/python3
"""
    Module with function that divides matrix elements
    by given divisor

"""


def matrix_divided(matrix, div):
    """Function that divides matrix elements by given divisor
    returns new_matrix
    """
    t_msg = "matrix must be a matrix (list of lists) of integers/floats"
    s_msg = "Each row of the matrix must have the same size"
    d_msg = "div must be a number"
    z_msg = "division by zero"

    if matrix:
        length = len(matrix[0])

    if not matrix or not isinstance(matrix, list):
        raise TypeError(t_msg)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(d_msg)
    if div == 0:
        raise ZeroDivisionError(z_msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(t_msg)
        if len(row) != length:
            raise TypeError(s_msg)
        for n in row:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError(t_msg)
    new_matrix = []
    for row in matrix:
        new_row = []
        for n in row:
            new_row.append(round(n / div, 2))
        new_matrix.append(new_row)

    return (new_matrix)
