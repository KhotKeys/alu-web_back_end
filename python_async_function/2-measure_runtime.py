#!/usr/bin/env python3


"""Measure the runtime"""
import time
import importlib
import asyncio

wait_n = importlib.import_module("1-concurrent_coroutines").wait_n
"""
import time module
import the concurrent_coroutines module
import the wait_n function
"""


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime

    Args:
    n (int): Number of times to spawn wait_random
    max_delay (int): Maximum delay for each wait_random call

    Returns:
    float: Total runtime
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
