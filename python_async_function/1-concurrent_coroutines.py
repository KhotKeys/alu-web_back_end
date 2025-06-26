#!/usr/bin/env python3

"""
Concurrent Coroutines
"""
import asyncio
from typing import List
import heapq
import importlib

wait_random = importlib.import_module("0-basic_async_syntax").wait_random
"""
import the random and asyncio libraries
from the 0-basic_async_syntax module
from the typing library import the List module
from the heapq library import the heapq module
from the importlib library import the importlib module
from the 0-basic_async_syntax module import the wait_random function
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified
    max_delay and return the list of delays in ascending order.

    Args:
    n (int): Number of times to spawn wait_random
    max_delay (int): Maximum delay for each wait_random call

    Returns:
    List[float]: List of delays in ascending order
    """
    # Create a list to store the tasks
    tasks = [wait_random(max_delay) for _ in range(n)]
    # Use asyncio.gather to run the tasks concurrently and get the results
    l1 = await asyncio.gather(*tasks)
    # Sorting a list without using sort function
    for i in range(0, len(l1)):
        for j in range(i + 1, len(l1)):
            if l1[i] >= l1[j]:
                l1[i], l1[j] = l1[j], l1[i]
    # Return the sorted list of delays
    return [heapq.heappop(l1) for _ in range(n)]
