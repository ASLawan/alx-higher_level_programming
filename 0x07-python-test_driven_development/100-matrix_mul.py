#!/usr/bin/python3
"""
    module with function that multiplies two matrices


"""


def matrix_mul(m_a, m_b):
    """
       Function that multiplies two matrices
    """
    a_msg = "m_a must be a list"
    b_msg = "m_b must be a list"
    a_list = "m_a must be a list of lists"
    b_list = "m_b must be a list of lists"
    a_mt = "m_a can't be empty"
    b_mt = "m_b can't be empty"
    t_a = "m_a should contain only integers or floats"
    t_b = "m_b should contain only integers or floats"
    s_a = "each row of m_a must be same size"
    s_b = "each row of m_b must be same size"
    m_msg = "m_a and m_b can't be multiplied"

    if not isinstance(m_a, list) and not isinstance(m_a, float):
        raise TypeError(a_msg)
    if not isinstance(m_b, list) and not isinstance(m_b, float):
        raise TypeError(b_msg)
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError(a_mt)
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise TypeError(b_mt)

    l1 = len(m_a[0])
    l2 = len(m_b[0])
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError(a_list)
        if len(row) != l1:
            raise TypeError(s_a)
        for n in row:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError(t_a)
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError(b_list)
        if len(row) != l2:
            raise TypeError(s_b)
        for n in row:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError(t_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError(m_msg)

    new_matrix = []
    rows = 0

    for row in m_a:
        new_row = []
        elem = 0
        value = 0
        while (elem < len(m_b[0])):
            value += row[rows] * m_b[rows][elem]
            if rows == len(m_b) - 1:
                rows = 0
                elem += 1
                new_row.append(value)
                value = 0
            else:
                rows += 1
        new_matrix.append(new_row)
    return new_matrix
