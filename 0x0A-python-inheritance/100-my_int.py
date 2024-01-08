#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """
    A class representing a rebel integer.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator (==).

        Args:
            other: The object to compare.

        Returns:
            bool: True if the values are not equal, False otherwise.

        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=).

        Args:
            other: The object to compare.

        Returns:
            bool: True if the values are equal, False otherwise.

        """
        return super().__eq__(other)
