#!/usr/bin/python3
""" models/base.py """

class Base:
    """ Base class for managing id attribute """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int): The id of the instance. If provided, it will be assigned to
                the `id` attribute. If not provided, a new id will be generated
                based on the current number of objects and assigned to the `id`
                attribute.

        Attributes:
            id (int): The id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objectsi
