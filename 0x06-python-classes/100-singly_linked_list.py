#!/usr/bin/python3
"""
This module defines two classes: Node and SinglyLinkedList.
"""

class Node:
    """
    Node represents a node in a singly linked list.
    Each node contains a data attribute and a reference to the next node.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Parameters:
            data (int): The data value to be stored in the node.
            next_node (Node): Reference to the next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data value of the node.

        Returns:
            int: The data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data value of the node.

        Parameters:
            value (int): The data value to be set.

        Raises:
            TypeError: If the value is not an integer.
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the reference to the next node.

        Returns:
            Node: The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node.

        Parameters:
            value (Node): The reference to the next node.

        Raises:
            TypeError: If the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList represents a singly linked list.
    It provides methods to manipulate the list, such as insertion and traversal.
    """
    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        current = self.head
        list_str = ""
        while current:
            list_str += str(current.data) + "\n"
            current = current.next_node
        return list_str

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into the linked list in sorted order.

        Parameters:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
