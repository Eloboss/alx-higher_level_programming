#!/usr/bin/python3
""" Create a new class Base """
from os import path
import json


class Base:
    """ New class base """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_ditionaries """
        new = []
        if list_dictionaries is None:
            return new
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a fils """
        filename = "{}.json".format(cls.__name__)
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                list_dictionaries.append(dictionary)
            json_string = Base.to_json_string(list_dictionaries)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        lst = []
        if json_string is None:
            return (lst)
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            new_c = cls(1, 1)
        if cls.__name__ == "Square":
            new_c = cls(1)
        new_c.update(**dictionary)
        return (new_c)

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)
        instance_list = []
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                dictionary_list = cls.from_json_string(json_string)
                for item in dictionary_list:
                    instance = cls.create(**item)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list
