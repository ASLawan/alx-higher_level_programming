#!/usr/bin/python3
""" Module for test Square class """
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareMethods(unittest.TestCase):
    """ Suite to test Square class """

    def setUp(self):
        """ Method to set environment for each test"""
        Base._Base__nb_objects = 0

    def test_new_square(self):
        """ Test square object """
        new_obj = Square(7)
        self.assertEqual(new_obj.size, 7)
        self.assertEqual(new_obj.width, 7)
        self.assertEqual(new_obj.height, 7)
        self.assertEqual(new_obj.x, 0)
        self.assertEqual(new_obj.y, 0)
        self.assertEqual(new_obj.id, 1)

    def test_new_square_2(self):
        """ Test square object with all attributes"""
        new_obj = Square(4, 5, 5, 7)
        self.assertEqual(new_obj.size, 4)
        self.assertEqual(new_obj.width, 4)
        self.assertEqual(new_obj.height, 4)
        self.assertEqual(new_obj.x, 5)
        self.assertEqual(new_obj.y, 5)
        self.assertEqual(new_obj.id, 7)

    def test_square_objects(self):
        """ Test multiple square objects"""
        new_obj1 = Square(4, 4)
        new_obj2 = Square(7, 7)
        self.assertEqual(False, new_obj1 is new_obj2)
        self.assertEqual(False, new_obj1.id == new_obj2.id)

    def test_instance_of_base(self):
        """ Test Square as instance Base class"""
        new_obj = Square(1)
        self.assertEqual(True, isinstance(new_obj, Base))

    def test_instance_of_rectangle(self):
        """ Test Square as instance of class Rectangle"""
        new_obj = Square(1)
        self.assertEqual(True, isinstance(new_obj, Rectangle))

    def test_incorrect_num_attrs(self):
        """ Test error raise with no args passed """
        with self.assertRaises(TypeError):
            new_obj = Square()

    def test_incorrect_num_attrs_1(self):
        """ Test error raised with no args passed """
        with self.assertRaises(TypeError):
            new_obj = Square(1, 1, 1, 1, 1)

    def test_private_attr_access(self):
        """ Trying to access to a private attribute """
        new_obj = Square(1)
        with self.assertRaises(AttributeError):
            new_obj.__width

    def test_private_attr_access_2(self):
        """ Trying to access to a private attribute """
        new_obj = Square(1)
        with self.assertRaises(AttributeError):
            new_obj.__height

    def test_private_attr_access_3(self):
        """ Trying to access to a private attribute """
        new_obj = Square(1)
        with self.assertRaises(AttributeError):
            new_obj.__x

    def test_private_attr_access_4(self):
        """ Trying to access to a private attribute """
        new_obj = Square(1)
        with self.assertRaises(AttributeError):
            new_obj.__y

    def test_valide_attributes(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new_obj = Square("2", 2, 2, 2)

    def test_valide_attributes_2(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new_obj = Square(2, "2", 2, 2)

    def test_valide_attributes_3(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new_obj = Square(2, 2, "2", 2)

    def test_attribute_value(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new_obj = Square(0)

    def test_attribute_value_2(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new_obj = Square(1, -1)

    def test_attribute_value_3(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new_obj = Square(1, 1, -1)

    def test_area(self):
        """ Checking the return value of area method """
        new_obj = Square(4)
        self.assertEqual(new_obj.area(), 16)

    def test_load_from_file(self):
        """ Test load JSON file """
        file = Square.load_from_file()
        self.assertEqual(file, file)

    def test_area_2(self):
        """ Checking the return value of area method """
        new_obj = Square(4)
        self.assertEqual(new_obj.area(), 16)
        new_obj.size = 7
        self.assertEqual(new_obj.area(), 49)

    def test_display(self):
        """ Test string printed """
        new_obj = Square(2)
        result = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_2(self):
        """ Test string printed """
        new_obj = Square(4)
        result = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

        new_obj.size = 5
        result = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_str(self):
        """ Test __str__ return value """
        new_obj = Square(4, 2, 2)
        result = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_str_2(self):
        """ Test __str__ return value """
        new_obj = Square(3, 2, 5, 3)
        result = "[Square] (3) 2/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

        new_obj.id = 1
        new_obj.size = 11
        result = "[Square] (1) 2/5 - 11\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_str_3(self):
        """ Test __str__ return value """
        new_obj = Square(5)
        result = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

        new_obj2 = Square(3, 7, 1)
        result = "[Square] (2) 7/1 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj2)
            self.assertEqual(str_out.getvalue(), result)

        new_obj3 = Square(1, 1, 1)
        result = "[Square] (3) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj3)
            self.assertEqual(str_out.getvalue(), result)

    def test_str_4(self):
        """ Test __str__ return value """
        new_obj = Square(3)
        result = "[Square] (1) 0/0 - 3"
        self.assertEqual(new_obj.__str__(), result)

    def test_display_3(self):
        """ Test string printed """
        new_obj = Square(5, 2, 1)
        result = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_4(self):
        """ Test string printed """
        new_obj = Square(3)
        result = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

        new_obj.x = 1
        result = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

        new_obj.y = 2
        result = "\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_update(self):
        """ Test update method """
        new_obj = Square(3)
        result = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

        new_obj.update(5)
        result = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_update_2(self):
        """ Test update method """
        new_obj = Square(3)
        result = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

        new_obj.update(5)
        result = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_update_3(self):
        """ Test update method """
        new_obj = Square(1)
        result = "[Square] (1) 0/0 - 1\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

        new_obj.update(2, 2, 2, 2)
        result = "[Square] (2) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

        new_obj.update(y=3)
        result = "[Square] (2) 2/3 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

        new_obj.update(id=1, size=10)
        result = "[Square] (1) 2/3 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_update_4(self):
        """ Test update method """
        new_obj = Square(10)
        result = "[Square] (1) 0/0 - 10\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

        dict = {'size': 3, 'y': 5}
        new_obj.update(**dict)
        result = "[Square] (1) 0/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_update_5(self):
        """ Test update method """
        new_obj = Square(7)
        result = "[Square] (1) 0/0 - 7\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

        dict = {'id': 10, 'x': '5', 'y': 5}

        with self.assertRaises(TypeError):
            new_obj.update(**dict)

    def test_to_dictionary(self):
        """ Test dictionary returned """
        new_obj = Square(1, 2, 3)
        result = "[Square] (1) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

        self.assertEqual(new_obj.size, 1)
        self.assertEqual(new_obj.width, 1)
        self.assertEqual(new_obj.height, 1)
        self.assertEqual(new_obj.x, 2)
        self.assertEqual(new_obj.y, 3)
        self.assertEqual(new_obj.id, 1)

        result = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(new_obj.to_dictionary()))
            self.assertEqual(str_out.getvalue(), result)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """
        new_obj = Square(2, 2, 2)
        result = "[Square] (1) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

        new_obj2 = Square(5)
        result = "[Square] (2) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj2)
            self.assertEqual(str_out.getvalue(), result)

        new_obj_dict = new_obj.to_dictionary()
        new_obj2.update(**new_obj_dict)

        self.assertEqual(new_obj.width, new_obj2.width)
        self.assertEqual(new_obj.height, new_obj2.height)
        self.assertEqual(new_obj.x, new_obj2.x)
        self.assertEqual(new_obj.y, new_obj2.y)
        self.assertEqual(new_obj.id, new_obj2.id)

        result = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(new_obj_dict))
            self.assertEqual(str_out.getvalue(), result)

    def test_dict_to_json(self):
        """ Test Dictionary to JSON string """
        new_obj = Square(2)
        dict = new_obj.to_dictionary()
        json_dict = Base.to_json_string([dict])
        result = "[{}]\n".format(dict.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dict)
            self.assertEqual(str_out.getvalue(), result.replace("'", "\""))

    def test_json_file(self):
        """ Test Dictionary to JSON string """
        new_obj = Square(2)
        dict = new_obj.to_dictionary()
        json_dict = Base.to_json_string([dict])
        result = "[{}]\n".format(dict.__str__())
        result = result.replace("'", "\"")

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dict)
            self.assertEqual(str_out.getvalue(), result)

        Square.save_to_file([new_obj])
        result = "[{}]".format(dict.__str__())
        result = result.replace("'", "\"")

        with open("Square.json", "r") as file:
            result2 = file.read()

        self.assertEqual(result, result2)

    def test_value_square(self):
        """ Test value pased to Square """
        with self.assertRaises(ValueError):
            new_obj = Square(-1)

    def test_create(self):
        """ Test create method """
        dict = {'id': 89}
        new_obj = Square.create(**dict)
        self.assertEqual(new_obj.id, 89)

    def test_create_2(self):
        """ Test create method """
        dict = {'id': 89, 'size': 1}
        new_obj = Rectangle.create(**dict)
        self.assertEqual(new_obj.id, 89)
        self.assertEqual(new_obj.size, 1)

    def test_create_3(self):
        """ Test create method """
        dict = {'id': 89, 'size': 1, 'x': 2}
        new_obj = Rectangle.create(**dict)
        self.assertEqual(new_obj.id, 89)
        self.assertEqual(new_obj.size, 1)
        self.assertEqual(new_obj.x, 2)

    def test_create_4(self):
        """ Test create method """
        dict = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        new_obj = Rectangle.create(**dict)
        self.assertEqual(new_obj.id, 89)
        self.assertEqual(new_obj.size, 1)
        self.assertEqual(new_obj.x, 2)
        self.assertEqual(new_obj.y, 3)

    def test_load_from_file_2(self):
        """ Test load JSON file """
        new_obj1 = Square(5)
        new_obj2 = Square(8, 2, 5)

        inpt = [new_obj1, new_obj2]
        Square.save_to_file(inpt)
        otpt = Square.load_from_file()

        for i in range(len(inpt)):
            self.assertEqual(inpt[i].__str__(), otpt[i].__str__())
