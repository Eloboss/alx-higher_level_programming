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

    def to_json(self):
        """ductionary like of self"""
        return self.__dict__
