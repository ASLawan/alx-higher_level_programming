#!/usr/bin/python3
"""Modeul with test cases for the Rectangle class methods"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangleMethods(unittest.TestCase):
    """Test suit for the Rectangle class"""

    def setUp(self):
        """Method that setups environment for test modules"""
        Base._Base__nb_objects = 0

    def test_new_object(self):
        """Method to test new object"""
        new_obj = Rectangle(6, 7)
        self.assertEqual(new_obj.width, 6)
        self.assertEqual(new_obj.height, 7)
        self.assertEqual(new_obj.x, 0)
        self.assertEqual(new_obj.y, 0)
        self.assertEqual(new_obj.id, 1)

    def test_new_object_2(self):
        """Method to test new object - all attributes"""
        new_obj = Rectangle(4, 8, 3, 2, 7)
        self.assertEqual(new_obj.width, 4)
        self.assertEqual(new_obj.height, 8)
        self.assertEqual(new_obj.x, 3)
        self.assertEqual(new_obj.y, 2)
        self.assertEqual(new_obj.id, 7)

    def test_compare_objs(self):
        """Method to compare to rectangle objects"""
        new_obj1 = Rectangle(4, 5)
        new_obj2 = Rectangle(6, 7)
        self.assertEqual(False, new_obj1 is new_obj2)
        self.assertEqual(False, new_obj1.id == new_obj2.id)

    def test_instance_of_object(self):
        """Method to test istance of object as Base"""
        new_obj = Rectangle(4, 8, 3, 2, 7)
        self.assertEqual(True, isinstance(new_obj, Base))

    def test_attr_number(self):
        """Test number of object attributes"""
        with self.assertRaises(TypeError):
            new_obj = Rectangle(7)

    def test_no_attrs(self):
        """Method to test for no attribute"""
        with self.assertRaises(TypeError):
            new_obj = Rectangle()

    def test_private_attr_access_width(self):
        """Method test for access to private attribut - width"""
        new_obj = Rectangle(6, 7)
        with self.assertRaises(AttributeError):
            new_obj.__width

    def test_private_attr_access_height(self):
        """Method test for access to private attribut - height"""
        new_obj = Rectangle(6, 7)
        with self.assertRaises(AttributeError):
            new_obj.__height

    def test_private_attr_access_x(self):
        """Method test for access to private attribut - x"""
        new_obj = Rectangle(6, 7)
        with self.assertRaises(AttributeError):
            new_obj.__x

    def test_private_attr_access_y(self):
        """Method test for access to private attribut - y"""
        new_obj = Rectangle(6, 7)
        with self.assertRaises(AttributeError):
            new_obj.__y

    def test_valid_input_width(self):
        """Method to test valid type for attribute - width"""
        with self.assertRaises(TypeError):
            new_obj = Rectangle('4', 8, 3, 2, 7)

    def test_valid_input_height(self):
        """Method to test valid type for attribute - height"""
        with self.assertRaises(TypeError):
            new_obj = Rectangle(4, '8', 3, 2, 7)

    def test_valid_input_x(self):
        """Method to test valid type for attribute - x"""
        with self.assertRaises(TypeError):
            new_obj = Rectangle(4, 8, '3', 2, 7)

    def test_valid_input_y(self):
        """Method to test valid type for attribute - y"""
        with self.assertRaises(TypeError):
            new_obj = Rectangle(4, 8, 3, '2', 7)

    def test_valid_input_1(self):
        """Method to test valid input for attribute - width"""
        with self.assertRaises(ValueError):
            new_obj = Rectangle(0, 8, 3, 2, 7)

    def test_valid_input_2(self):
        """Method to test for valid input for attribute - height"""
        with self.assertRaises(ValueError):
            new_obj = Rectangle(4, 0, 3, 2, 7)

    def test_valid_input_3(self):
        """Method to test for valid input for attribute - x"""
        with self.assertRaises(ValueError):
            new_obj = Rectangle(4, 8, -3, 2, 7)

    def test_valid_input_4(self):
        with self.assertRaises(ValueError):
            new_obj = Rectangle(4, 8, 3, -2, 7)

    def test_area_1(self):
        """Method to test area of object"""
        new_obj = Rectangle(4, 8)
        self.assertEqual(new_obj.area(), 32)

    def test_area_2(self):
        """Test area with re-assigned width and height"""
        new_obj = Rectangle(4, 8)
        self.assertEqual(new_obj.area(), 32)
        new_obj.width = 5
        self.assertEqual(new_obj.area(), 40)
        new_obj.height = 10
        self.assertEqual(new_obj.area(), 50)

    def test_area_3(self):
        """Method to test area of objects"""
        new_obj1 = Rectangle(2, 4)
        self.assertEqual(new_obj1.area(), 8)
        new_obj2 = Rectangle(7, 7)
        self.assertEqual(new_obj2.area(), 49)

    def test_display(self):
        """Method to test object display"""
        new_obj = Rectangle(3, 4)
        result = "###\n###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_2(self):
        new_obj = Rectangle(3, 3)
        result = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

        new_obj.height = 4
        result = "###\n###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_3(self):
        """Test object display method"""
        new_obj = Rectangle(3, 4, 1, 1)
        result = "\n ###\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_format_4(self):
        """Test object format - resassign width and height"""
        new_obj = Rectangle(2, 3)
        result = "##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

        new_obj.x = 3
        result = "   ##\n   ##\n   ##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

        new_obj.y = 3
        result = "\n\n\n   ##\n   ##\n   ##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new_obj.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_format(self):
        """Method to test the format string method"""
        new_obj = Rectangle(4, 8, 3, 2)
        result = "[Rectangle] (1) 3/2 - 4/8\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_format_2(self):
        """Mthod to test string formating"""
        new_obj = Rectangle(4, 8, 3, 2, 7)
        result = "[Rectangle] (7) 3/2 - 4/8\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

        new_obj.id = 1
        new_obj.width = 2
        new_obj.height = 4
        result = "[Rectangle] (1) 3/2 - 2/4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

    def test_format_3(self):
        """Test object format"""
        new_obj1 = Rectangle(2, 4)
        result = "[Rectangle] (1) 0/0 - 2/4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj1)
            self.assertEqual(str_out.getvalue(), result)

        new_obj2 = Rectangle(2, 4, 3, 2)
        result = "[Rectangle] (2) 3/2 - 2/4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj2)
            self.assertEqual(str_out.getvalue(), result)

        new_obj3 = Rectangle(7, 7, 7, 7)
        result = "[Rectangle] (3) 7/7 - 7/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj3)
            self.assertEqual(str_out.getvalue(), result)

    def test_format_4(self):
        """Test object print format"""
        new_obj = Rectangle(7, 7)
        result = "[Rectangle] (1) 0/0 - 7/7"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(new_obj.__str__(), result)

    def test_to_dictionary(self):
        """Test dictionary method"""
        new_obj = Rectangle(4, 8, 3, 2, 7)
        result = "[Rectangle] (7) 3/2 - 4/8\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj)
            self.assertEqual(str_out.getvalue(), result)

        self.assertEqual(new_obj.width, 4)
        self.assertEqual(new_obj.height, 8)
        self.assertEqual(new_obj.x, 3)
        self.assertEqual(new_obj.y, 2)
        self.assertEqual(new_obj.id, 7)
        result = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(new_obj.to_dictionary()))
            self.assertEqual(str_out.getvalue(), result)

    def test_to_dictionary_2(self):
        """Test the to_dictionary method"""
        new_obj1 = Rectangle(2, 2, 2, 2)
        result = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj1)
            self.assertEqual(str_out.getvalue(), result)

        new_obj2 = Rectangle(5, 7)
        result = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(new_obj2)
            self.assertEqual(str_out.getvalue(), result)

        new_dict1 = new_obj1.to_dictionary()
        new_obj2.update(**new_dict1)

        self.assertEqual(new_obj1.width, new_obj2.width)
        self.assertEqual(new_obj1.height, new_obj2.height)
        self.assertEqual(new_obj1.x, new_obj2.x)
        self.assertEqual(new_obj1.y, new_obj2.y)
        self.assertEqual(new_obj1.id, new_obj2.id)
        result = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(new_dict1))
            self.assertEqual(str_out.getvalue(), result)

    def test_dict_to_string(self):
        """Test dictionary to string method"""
        new_obj = Rectangle(4, 8)
        dict = new_obj.to_dictionary()
        json_dict = Base.to_json_string([dict])
        res = "[{}]\n".format(dict.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dict)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_check_value(self):
        """Test arguments passed"""
        with self.assertRaises(ValueError):
            new_obj = Rectangle(-4, 8)

    def test_check_value_2(self):
        """Test arguments passed"""
        with self.assertRaises(ValueError):
            new_obj = Rectangle(4, -8)

    def test_create(self):
        """Test create method"""
        dict = {'id': 7}
        new_obj = Rectangle.create(**dict)
        self.assertEqual(new_obj.id, 7)

    def test_create_2(self):
        """Test create method"""
        dict = {'id': 7, 'width': 4}
        new_obj = Rectangle.create(**dict)
        self.assertEqual(new_obj.id, 7)
        self.assertEqual(new_obj.width, 4)

    def test_create_3(self):
        """Test create method"""
        dict = {'id': 7, 'width': 4, 'height': 8}
        new_obj = Rectangle.create(**dict)
        self.assertEqual(new_obj.id, 7)
        self.assertEqual(new_obj.width, 4)
        self.assertEqual(new_obj.height, 8)

    def test_create_4(self):
        """Test create method"""
        dict = {'id': 7, 'width': 4, 'height': 8, 'x': 3}
        new_obj = Rectangle.create(**dict)
        self.assertEqual(new_obj.id, 7)
        self.assertEqual(new_obj.width, 4)
        self.assertEqual(new_obj.height, 8)
        self.assertEqual(new_obj.x, 3)

    def test_create_5(self):
        """Test create method"""
        dict = {'id': 7, 'width': 4, 'height': 8, 'x': 3, 'y': 2}
        new_obj = Rectangle.create(**dict)
        self.assertEqual(new_obj.id, 7)
        self.assertEqual(new_obj.width, 4)
        self.assertEqual(new_obj.height, 8)
        self.assertEqual(new_obj.x, 3)
        self.assertEqual(new_obj.y, 2)

    def test_load_from_file(self):
        """Test load_from_file method"""
        file = Rectangle.load_from_file()
        self.assertEqual(file, [])

    def test_load_from_file_2(self):
        """Test load from file method"""
        new_obj1 = Rectangle(4, 8)
        new_obj2 = Rectangle(4, 8, 3, 2)
        inpt = [new_obj1, new_obj2]
        Rectangle.save_to_file(inpt)
        otpt = Rectangle.load_from_file()

        for i in range(len(inpt)):
            self.assertEqual(inpt[i].__str__(), otpt[i].__str__())
