#!/usr/bin/python3
"""Two classes are going to be defined"""


class Node:
    """defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """intialisation
        Args:
            data (int): data saved in a node
            next_node: next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter func"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter func"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """getter func"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter func"""
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """defines a singly linked list """

    def __init__(self):
        """initialisation"""
        self.__head = None

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
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
