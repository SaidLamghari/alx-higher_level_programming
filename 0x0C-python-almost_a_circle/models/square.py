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
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
