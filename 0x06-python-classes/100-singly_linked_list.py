#!/usr/bin/python3
"""
This module defines two classes: Node and SinglyLinkedList.
"""

class Node:
    """
    Node represents a node of a singly linked list.

    Attributes:
        __data (int): The data value stored in the node.
        __next_node (Node): Reference to the next node in the list.

    Args:
        data (int): The data value to be stored in the node.
        next_node (Node, optional): The next node in the list. Defaults to None.
    """

    def __init__(self, data, next_node=None):
        self.__data = None
        self.__next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data value of the node.

        Returns:
            int: The data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the data value of the node.

        Args:
            value (int): The data value to be set.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next node in the list.

        Returns:
            Node: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next node in the list.

        Args:
            value (Node): The next node in the list.

        Raises:
            TypeError: If the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList represents a singly linked list.

    Attributes:
        head (Node): The head of the linked list.

    Methods:
        __init__: Initializes a new instance of the SinglyLinkedList class.
        __str__: Returns a string representation of the linked list.
        sorted_insert: Inserts a new Node into the correct sorted position in the list (increasing order).
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
        return list_str.rstrip()  # Remove trailing newline

    def sorted_insert(self, value):
        """
        Inserts a new Node with the given value into the linked list in the correct sorted position.

        Args:
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
