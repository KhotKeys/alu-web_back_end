#!/usr/bin/env python3


"""
    This script imports the Callable module.
"""
from typing import Callable

"""
    This script calculates the factorial of a number.
    It takes an integer as input and returns a function
    that multiplies its argument by multiplier.
    """


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its argument by multiplier.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        callable: A function that multiplies its argument by multiplier.
    """
    return lambda x: x * multiplier
