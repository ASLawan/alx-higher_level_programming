#!/usr/bin/python3
"""
    Module with class Base


"""
import json
import csv
import os.path
import turtle


class Base:
    """Class Base that defines base objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method that initialiases object attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns JSON string representation
            of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes JSON string representation of
            list_obj to a file
        """
        filename = "{}.json".format(cls.__name__)
        list_dict = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dict)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of JSON string representation"""
        if not json_string or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method that returns an instance with all atributes already set"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(10, 10)
        else:
            new_instance = cls(10)

        new_instance.update(**dictionary)

        return new_instance

    @classmethod
    def load_from_file(cls):
        """method that returns list of instances"""
        file = "{}.json".format(cls.__name__)
        try:
            with open(file, 'r') as f:
                json_string = f.read()
                list_dict = cls.from_json_string(json_string)
                list_instances = [cls.create(**dict) for dict in list_dict]
                return list_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV file """
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])
        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        filename = "{}.csv".format(cls.__name__)
        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']
        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Method that draws instance objects"""
        screen = turtle.Screen()
        screen.bgcolor("white")

        t = turtle.Turtle()

        for rect in list_rectangles:
            t.penup()
            t.gpto(rectangle("x"), rectangle["y"])
            t.pendown()
            t.forward(rectangle["width"])
            t.right(90)
            t.forward(rectangle["height"])
            t.right(90)
            t.forward(rectangle["width"])
            t.right(90)
            t.forward(rectangle["height"])
            t.right(90)

        for sqr in list_squares:
            t.penup()
            t.goto(sqaure["x"], square["y"])
            t.pendown()
            for _ in range(4):
                t.forward(square["size"])
                t.right(90)

        t.hideturtle()
        turtle.done()
