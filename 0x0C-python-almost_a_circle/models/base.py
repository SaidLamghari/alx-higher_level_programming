#!/usr/bin/python3
""" models/base.py """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to its JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.

        Note:
            If list_dictionaries is None or empty, the string "[]" is returned.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
