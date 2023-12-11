#!/usr/bin.python
"""Test case for the class Base"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch
import os


class TestBaseClass(unittest.TestCase):
    """Base class test suit"""

    def setUp(self):
        """Model to setup environment for each test case"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test object id"""
        new_obj = Base(1)
        self.assertEqual(new_obj.id, 1)

    def test_default_id(self):
        """Test default object id"""
        new_obj = Base()
        self.assertEqual(new_obj.id, 1)

    def test_default_id_2(self):
        """Test class attribute number of objects to object id"""
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_assigned_ids(self):
        """Test different assigned ids"""
        new_obj1 = Base()
        new_obj2 = Base(7)
        new_obj3 = Base()
        self.assertEqual(new_obj1.id, 1)
        self.assertEqual(new_obj2.id, 7)
        self.assertEqual(new_obj3.id, 2)

    def test_string_as_id(self):
        """Test a string as object id"""
        new_obj = Base('7')
        self.assertEqual(new_obj.id, '7')

    def test_more_args(self):
        """Test for more than 1 argument"""
        with self.assertRaises(TypeError):
            new_obj = Base(7, 7)

    def test_private_attr_access(self):
        """Test accesibility of private class attribute"""
        new_obj = Base()
        with self.assertRaises(AttributeError):
            new_obj.__nb__objects

    def test_square_save_to_file(self):
        """Test the save_to_file method for square object"""
        Square.save_to_file(None)
        result = "[]\n"
        with open("Square.json", "r") as f:
            with patch("sys.stdout", new=StringIO()) as str_out:
                print(f.read())
                self.assertEqual(str_out.getvalue(), result)
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_rectangle_save_to_file(self):
        """Test the save_to_file method for rectangle object"""
        Rectangle.save_to_file(None)
        result = "[]\n"
        with open("Rectangle.json", "r") as f:
            with patch("sys.stdout", new=StringIO()) as str_out:
                print(f.read())
                self.assertEqual(str_out.getvalue(), result)
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
