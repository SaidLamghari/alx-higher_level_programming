#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""

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
