#!/usr/bin/python3
"""Describe a singly linked list"""


class Node:
    """Represent a node."""
    def __init__(self, data, next_node=None):
        """Node with attributes
        args:
            data: Variable stored
            next_node: Next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data."""
        return self.__data

    @data.setter
    def data(self, value):
        """"To set the data."""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """"Retrieves d node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets d node attributes"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly linked class."""
    def __init__(self):
        """initializes self."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node in correct position
        args:
            value: position
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
