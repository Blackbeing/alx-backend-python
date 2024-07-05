#!/usr/bin/env python3

"""Function to return safe first element"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first object or None"""
    if lst:
        return lst[0]
    else:
        return None
