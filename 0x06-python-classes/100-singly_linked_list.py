#!/usr/bin/python3
"""class Node that defines a node of a singly linked list"""


class Node:
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    def get_data(self):
        return self.__data

    def set_data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    def get_next_node(self):
        return self.__next_node

    def set_next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or value < self.__head.get_data():
            new_node.set_next_node(self.__head)
            self.__head = new_node
        else:
            current = self.__head
            while current.get_next_node() is not None and current.get_next_node().get_data() < value:
                current = current.get_next_node()
            new_node.set_next_node(current.get_next_node())
            current.set_next_node(new_node)

    def __str__(self):
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.get_data()) + "\n"
            current = current.get_next_node()
        return result
