#!/usr/bin/python3
"""A function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list): A matrix represented as a list of lists.
        div (int or float): The number to divide each element of the matrix by.

    Returns:
        list: The matrix with all elements divided by the given number.

    Raises:
        TypeError: If the matrix is not a valid matrix or if the div is not a number.
        ZeroDivisionError: If the div is zero.

    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0

    if num_rows == 0 or num_cols == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == num_cols for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/2-matrix_divided.txt")
