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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.

        Note:
            If list_objs is None, an empty list is saved.
            The filename is <Class name>.json, where Class name is the name of the class of the instances.
            The file is overwritten if it already exists.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string.

        Note:
            If json_string is None or empty, an empty list is returned.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

