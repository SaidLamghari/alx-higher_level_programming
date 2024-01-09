#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""

import sys


def print_stats(total_size, status_codes):
    """
    Prints the statistics based on the total file size and status code counts.

    Args:
        total_size (int): The total file size.
        status_codes (dict): A dictionary containing status codes as keys
            and their corresponding counts as values.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        count = status_codes[code]
        print("{}: {}".format(code, count))

def parse_line(line):
    """
    Parses a line of input and extracts the file size and status code.

    Args:
        line (str): The line of input.

    Returns:
        tuple: A tuple containing the file size (int) and status code (str).
    """
    parts = line.split()
    return int(parts[-1]), parts[-2]

def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            file_size, status_code = parse_line(line)
            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
