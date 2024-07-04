#!/usr/bin/env python3
"""Sum list of floats and ints"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum list of floats and ints"""
    return sum(mxd_lst)
