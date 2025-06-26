#!/usr/bin/env python3


"""Basic async syntax example"""
import random
import asyncio

"""import the random and asyncio libraries"""


async def wait_random(max_delay: int = 10) -> float:
    """returns the float of a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
