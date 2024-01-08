#!/usr/bin/python3
"""function that prints a text with 2 new lines
after each of these characters: ., ? and :
    """


def text_indentation(text):
    """
    Prints the text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Filter out leading and trailing whitespaces
    text = text.strip()

    # Define the characters that should be followed by 2 new lines
    punctuation_marks = ['.', '?', ':']

    # Iterate through each character in the text
    for char in text:
        print(char, end="")
        if char in punctuation_marks:
            print("\n\n", end="")

if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/5-text_indentation.txt")

