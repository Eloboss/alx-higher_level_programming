#!/usr/bin/python3


class LockedClass:
    """To detect errors"""
    def __setattr__(self, name, value):
        """loced class with attributes"""
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '" +
                                 name + "'")

    def __getattr__(self, name):
        if name == "__dict__":
            raise AttributeError("'LockedClass' object has no attribute '" +
                                 name + "'")
