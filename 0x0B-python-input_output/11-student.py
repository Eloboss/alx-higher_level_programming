#!/usr/bin/python3
"""student to json"""


class Student:
    """student attributes"""
    def __init__(self, first_name, last_name, age):
        """initialises the student
        args:
            first_name = first name of student
            last_bame = last name of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ductionary like of self"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
         """replaces all attributes of the Student instance"""
         for elo, boss in json.items():
            setattr(self, elo, boss)
