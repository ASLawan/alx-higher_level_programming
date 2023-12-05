#!/usr/bin/python3
"""
    Module with function that implements the
    Pascal's triangle

"""


def pascal_triangle(n):
    """function that prints Pascal's triangle"""
    if n <= 0:
        return []
    pt = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pt[i - 1][j - 1] + pt[i - 1][j])
        row.append(1)
        pt.append(row)

    return pt
