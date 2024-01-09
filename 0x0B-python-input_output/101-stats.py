#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""

import sys
import random
import time


status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
file_sizes = [random.randint(100, 1000) for _ in range(100)]


def generate_log_line():
    status_code = random.choice(status_codes)
    file_size = random.choice(file_sizes)
    return f"{status_code} {file_size}"


def main():
    total_size = 0
    status_code_counts = {}

    try:
        while True:
            log_line = generate_log_line()
            file_size, status_code = log_line.split()
            total_size += int(file_size)
            status_code_counts[status_code] = status_code_counts.get(
                    status_code, 0) + 1

            # Check for a stop condition
            if total_size >= 1000000 or status_code_counts.get("404", 0) >= 10:
                break

            # Print statistics every 10 lines
            if len(status_code_counts) % 10 == 0:
                print("File size: {}".format(total_size))
                for code, count in sorted(status_code_counts.items()):
                    print("{}: {}".format(code, count))

            # Simulate delay between log lines
            time.sleep(random.random())

    except KeyboardInterrupt:
        pass

    # Print final statistics
    print("File size: {}".format(total_size))
    for code, count in sorted(status_code_counts.items()):
        print("{}: {}".format(code, count))

    # Check if stop condition was met
    if total_size >= 1000000:
        print("Stop condition: Total file size reached 1MB")
    elif status_code_counts.get("404", 0) >= 10:
        print("Stop condition: 10 or more occurrences of status code 404")


if __name__ == "__main__":
    main()
