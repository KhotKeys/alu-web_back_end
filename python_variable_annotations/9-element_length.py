#!/usr/bin/env python3

"""Import List and Tuple"""
from typing import List, Tuple, Iterable, Sequence

"""
This module contains a function that
returns a list of tuples, where each tuple
contains an element from the input list and its length.

Example:
    >>> element_length([[1, 2, 3], [4, 5], [6]])
    [([1, 2, 3], 3), ([4, 5], 2), ([6], 1)]
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an
    element from the input list and its length.

    Args:
        lst (List[List[Any]]): The input list.

    Returns:
        List[Tuple[List[Any], int]]: The list of tuples.

    Example:
        >>> element_length([[1, 2, 3], [4, 5], [6]])
        [([1, 2, 3], 3), ([4, 5], 2), ([6], 1)]
    """
    return [(i, len(i)) for i in lst]
