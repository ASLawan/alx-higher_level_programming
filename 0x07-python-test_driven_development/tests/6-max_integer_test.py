#!/usr/bin/python3
"""unittest module for max_integer function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max integer"""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "Austin"])

    def test_repeated_elements(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_zero_number_list(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_tuple_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([15, (20, 25)])

    def test_string_number(self):
        with self.assertRaises(TypeError):
            max_integer([9, 8, '7'])

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)


if __name__ == "__main__":
    unittest.main()
