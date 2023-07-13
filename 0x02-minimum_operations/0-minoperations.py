#!/usr/bin/python3

"""
minimum operation
"""


def minOperations(n):
    """
    minimum operation function
    """
    if n == 1:
        return 0  # No operations needed for a single 'H'

    operations = 0
    factor = 2  # Represents the number of 'H's currently in the file

    while factor <= n:
        if n % factor == 0:
            n //= factor
            operations += factor
        else:
            factor += 1

    return operations
