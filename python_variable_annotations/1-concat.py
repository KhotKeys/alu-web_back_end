#!/usr/bin/env python3


"""
This module contains a function that
concatenates two strings.
The function takes two strings as arguments and
returns a concatenated string

Example:
    >>> concat("Hello ", "World!")
    'Hello World!'
    >>> concat("Hello ", 42)
    'Hello 42'
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the result.

    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The concatenated string.

    Example:
        >>> concat("Hello ", "World!")
        'Hello World!'
    """

    return str1 + str2
