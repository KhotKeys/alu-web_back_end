#!/usr/bin/env python3


"""
    This script imports the Union and Tuple modules.
"""
from typing import Union, Tuple

"""
    This script calculates the factorial of a number.
    It takes an integer as input and returns a tuple
    of the number and its factorial.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a dictionary with keys k and values v."""
    return k, float(v) ** 2
