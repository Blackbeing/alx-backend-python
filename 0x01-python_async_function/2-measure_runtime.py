#!/usr/bin/env python3
"""Module to measure execution time of function"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure execution time of function"""
    begin = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    exec_time = end - begin
    return exec_time
