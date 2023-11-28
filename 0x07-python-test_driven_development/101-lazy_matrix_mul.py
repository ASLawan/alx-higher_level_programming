#!/usr/bin/python3
"""
    Module with function that multipies two matrices
    using pythons built-in Numpy

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        Function to multiply two matrices using Numpy
    """
    return np.matmul(m_a, m_b)
