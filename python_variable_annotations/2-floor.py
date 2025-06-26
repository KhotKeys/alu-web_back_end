#!/usr/bin/env python3


"""
This module contains a function that
rounds a float down to the nearest integer.

Example:
    >>> floor(3.14)
    3
    >>> floor(-3.14)
    -4
"""


def floor(n: float) -> int:
    """
    Round a float down to the nearest integer.

    Args:
        n (float): The float to round down.

    Returns:
        int: The rounded down integer.

    Example:
        >>> floor(3.14)
        3
        >>> floor(-3.14)
        -4
    """
    return int(n)
