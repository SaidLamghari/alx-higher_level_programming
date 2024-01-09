#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read (optional).
                        If no filename is provided,
                        the function will attempt to read
                        from a file named "filename".

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.

    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
