#!/usr/bin/env python3
"""This module provides test for utils"""

import unittest
from parameterized import parameterized
from typing import Dict, Union, Tuple
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Use parameterized testing to test nested map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: dict, path: Tuple[str], expected: Union[Dict, int]
    ):
        """Test the function using parameterized objects"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
