#!/usr/bin/env python3
"""Wait random module using async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait using async.
    Return time waited
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
