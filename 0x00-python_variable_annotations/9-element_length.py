#!/usr/bin/env python3

"""Function to annotate return value"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns iterable"""
    return [(i, len(i)) for i in lst]
