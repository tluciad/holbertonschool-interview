#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file."""
    copy = 1
    paste = 0
    result = 0

    if (n <= 0):
        return (0)

    while copy < n:
        if n % copy == 0:
            paste = copy
            copy *= 2
            result += 1
        else:
            copy += paste
        result += 1

    return result
