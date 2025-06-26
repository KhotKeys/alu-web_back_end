#!/usr/bin/env python3


"""
    A normal function that returns a coroutine object
    that takes an integer as argument
"""
import asyncio
import importlib

wait_random = importlib.import_module("0-basic_async_syntax").wait_random
"""
import the random and asyncio libraries
from the 0-basic_async_syntax module
import wait_random function
"""


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    returns the a task of a random delay
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
