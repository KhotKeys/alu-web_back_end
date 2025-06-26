#!/usr/bin/env python3


"""
This module contains a function that
sums all elements in a list.
import List from typing
"""
from typing import Union, List


"""
This module contains a function that
sums all elements in a list.

Example:
    >>> sum_mixed_list([1, 2, 3, 4])
    10
    >>> sum_mixed_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    55
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of all elements in a list.

    Args:
        mxd_lst (list): The list to sum.

    Returns:
        float: The sum of all elements in the list.

    Example:
        >>> sum_mixed_list([1, 2, 3, 4])
        10
    """
    return sum(mxd_lst)
