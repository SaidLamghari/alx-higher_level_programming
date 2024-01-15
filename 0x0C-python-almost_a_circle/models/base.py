#!/usr/bin/python3
""" models/base.py """
import json
import csv


class Base:
    """ Base class for managing id attribute """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Attributes:
            id (int): The id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

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
            The filename is <Class name>.json, where
            Class name is the name of the class of the instances.
            The file is overwritten if it already exists.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary()\
                for obj in list_objs])
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by
        the JSON string representation json_string.

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

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes
        already set based on the provided dictionary.

        Args:
            **dictionary: A double pointer to
            a dictionary containing attribute values.

        Returns:
            Base: An instance with attributes set based on the dictionary.

        Note:
            The **dictionary is treated as **kwargs for the update method.
    """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            copy = Rectangle(1, 1)
        elif cls is Square:
            copy = Square(1)
        else:
            copy = None
        copy.update(**dictionary)
        return copy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a JSON file.

        Returns:
            list: A list of instances of the current class.

        Note:
            The filename is <Class name>.json, where Class name is
            the name of the class of the instances.
            If the file doesn't exist, an empty list is returned.
            The method uses the from_json_string and create
            methods to load and create the instances.
        """
        from os import path
        filename = f"{cls.__name__}.json"
        if not os.path.isfile(filename):
            return []
        with open(filename, "r", encoding="utf-8") as fle:
            return [cls.create(**d) for d in cls.from_json_string(fle.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects to a CSV file.

        Args:
            list_objs (list): A list of objects to serialize.

        """
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[objs.id, objs.width, objs.height, objs.x, objs.y]
                             for objs in list_objs]
            else:
                list_objs = [[objs.id, objs.size, objs.x, objs.y]
                             for objs in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as fle:
            writer = csv.writer(fle)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes objects from a CSV file.

        Returns:
            list: A list of deserialized objects.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        retour = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='',
                  encoding='utf-8') as fle:
            reader = csv.reader(fle)
            for row in reader:
                row = [int(i) for i in row]
                if cls is Rectangle:
                    dict = {"id": row[0], "width": row[1], "height":
                            row[2], "x": row[3], "y": row[4]}
                else:
                    dict = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                retour.append(cls.create(**dict))
        return retour
