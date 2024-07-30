#!/usr/bin/env python3
"""This module provides test for utils"""

import unittest
from parameterized import parameterized
from typing import Dict, Union, Tuple
from utils import access_nested_map, get_json, memoize
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

    @parameterized.expand([
        ({}, ("a",), KeyError), ({"a": 1}, ("a", "b"), KeyError)
    ])
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
        """Test get json method using patch"""
        mock_obj = Mock()
        mock_obj.json.return_value = test_payload
        with patch("requests.get", return_value=mock_obj) as req:
            self.assertEqual(get_json(test_url), test_payload)
            req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test Memoization in python"""

    def test_memoize(self):
        """Test method for memoization"""

        class TestClass:
            """Dummy class to test memoization"""

            def a_method(self):
                """ "Dummy method to test memoization"""
                return 42

            @memoize
            def a_property(self):
                """Function to memoize a function call"""
                return self.a_method()

        with patch.object(
            TestClass, "a_method", return_value=lambda: 42
        ) as memoized_fn:
            klass = TestClass()
            self.assertEqual(klass.a_property(), 42)
            self.assertEqual(klass.a_property(), 42)
            memoized_fn.assert_called_once()
