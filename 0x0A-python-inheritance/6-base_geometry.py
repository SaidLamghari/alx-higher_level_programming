#!/usr/bin/python3
"""a class BaseGeometry (based on 5-base_geometry.py)."""


class BaseGeometry:
    """
    A base class for geometry-related classes.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: Indicates that the `area`
            method is not implemented in the derived class.

        """
        raise Exception("area() is not implemented")
