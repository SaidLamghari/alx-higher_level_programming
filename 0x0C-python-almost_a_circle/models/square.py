#!/usr/bin/python3
""" models/square.py """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The id of the square. If not provided,
                        it will be handled by the Rectangle class.

        Attributes:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The id of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns the string representation of the square """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
            self.x, self.y, self.width))

    @property
    def size(self):
        """ Getter for the size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """
        Method that updates instance attributes
        """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """
        Update the class Square by adding the public method
        """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.

        Returns:
            dict: A dictionary containing the attributes of the Square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
