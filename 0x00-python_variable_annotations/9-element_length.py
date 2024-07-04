#!/usr/bin/env python3

"""Function to annotate return value"""
from typing import Sequence, List, Tuple


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    """Returns iterable"""
    return [(i, len(i)) for i in lst]
