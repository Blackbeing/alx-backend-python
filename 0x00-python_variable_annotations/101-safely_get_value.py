#!/usr/bin/env python3
"""Get value or default"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """get value or default"""
    if key in dct:
        return dct[key]
    else:
        return default
