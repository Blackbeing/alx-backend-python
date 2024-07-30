#!/usr/bin/env python3
"""This module provides test for utils"""

import unittest
from parameterized import parameterized
from typing import Dict, Union, Tuple
from utils import access_nested_map, get_json
from unittest.mock import Mock, patch


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

    @parameterized.expand([({}, ("a",), KeyError), ({"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(
        self, nested_map: dict, path: Tuple[str], exception: Exception
    ):
        """Use parameterized testing to test nested map"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url: str, test_payload: Dict):
        mock_obj = Mock()
        mock_obj.json.return_value = test_payload
        with patch("requests.get", return_value=mock_obj) as req:
            self.assertEqual(get_json(test_url), test_payload)
            req.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
