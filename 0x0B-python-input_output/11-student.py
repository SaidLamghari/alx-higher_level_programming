#!/usr/bin/python3
""" a class Student that defines a student by:
    (based on 10-student.py)"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        Attributes:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attribute names. If provided,
                only the attribute names contained in this list will be
                retrieved. Defaults to None.

        Returns:
            dict: A dictionary representing the Student instance, with the
                keys as attribute names and the values as their corresponding
                values from the instance. If attrs is provided, only the
                specified attributes are included in the dictionary.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with the values
        from the provided dictionary.

        Args:
            json (dict): A dictionary containing attribute names as keys
                and their corresponding values.
        """
        for keys, values in json.items():
            setattr(self, keys, values)
