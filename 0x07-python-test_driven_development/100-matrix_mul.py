#!/usr/bin/python3
"""function that multiplies 2 matrices:"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.

    Args:
        m_a (list): The first matrix as a list of lists.
        m_b (list): The second matrix as a list of lists.

    Returns:
        list: The resulting matrix as a list of lists.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists.
        ValueError: If m_a or m_b is empty or if the matrices cannot be multiplied.
        TypeError: If m_a or m_b contains non-integer or non-float elements.
        TypeError: If m_a or m_b is not a rectangle.
    """
    # Validate m_a and m_b
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists and m_b must be a list of lists")

    if m_a == [] or m_b == []:
        raise ValueError("m_a can't be empty and m_b can't be empty")

    if not all(isinstance(element, (int, float)) for row in m_a for element in row) or not all(
            isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_a should contain only integers or floats and m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size and each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
