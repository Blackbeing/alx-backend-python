#!/usr/bin/env python3
"""type_checking module"""
from typing import Tuple, Union, List, Sequence


def zoom_array(lst: Sequence,
               factor: Union[float, int] = 2) -> Sequence:
    """Returns zoomed in list"""
    zoomed_in: Union[List, Tuple] = [
        item for item in lst for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
