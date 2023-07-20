#!/usr/bin/python3

"""
log parsing
"""

import sys


def print_statistics(file_sizes, status_codes):

    """
    a script that reads stdin line by line and computes metrics
    """

    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")

    for status_code in sorted(status_codes):
        if isinstance(status_code, int):
            count = status_codes[status_code]
            print(f"{status_code}: {count}")


def main():

    """
    computes input output
    """

    file_sizes = []
    stat_cod = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_counter = 0

    try:
        for line in sys.stdin:
            line_counter += 1

            # Skip lines with incorrect format
            if 'GET /projects/260 HTTP/1.1' not in line:
                continue

            parts = line.split()
            if len(parts) >= 9:
                try:
                    status_code = int(parts[-2])
                    file_size = int(parts[-1])
                    file_sizes.append(file_size)
                    stat_cod[status_code] += 1
                except ValueError:
                    pass

            # Print statistics every 10 lines
            if line_counter % 10 == 0:
                print_statistics(file_sizes, stat_cod)

    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (CTRL + C)
        print_statistics(file_sizes, stat_cod)


if __name__ == "__main__":
    main()
