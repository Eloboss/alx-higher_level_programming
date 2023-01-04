#!/usr/bin/python3


class LockedClass:
    """To detect errors"""
    def __setattr___(self, name):
        """locked class with attributes"""
        if name == "first_name":
            raise AttributeError("'LockedClass' object has no attribute'" + name +"'")
