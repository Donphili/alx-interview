#!/usr/bin/python3


def minOperations(n):
    """
    Calculates the fewest number of operations needed to transform 'H' to 'n' 'H' characters.
    :param n: Integer, the target number of 'H' characters.
    :return: Integer, the fewest number of operations.
    """
    if n <= 1:
        return 0

    operations = 0
    current_h = 1
    clipboard = 0

    while current_h < n:
        if n % current_h == 0:
            clipboard = current_h
        current_h += clipboard
        operations += 1

    return operations
