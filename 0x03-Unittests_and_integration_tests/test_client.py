#!/usr/bin/env python3
"""Parameterized mock test for requests"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Class to test github org client
    """

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, input, mock_get_json):
        """
        Test case to validate the GithubOrgClient class for fetching
        organization data.

        Parameters:
        - org (str): The name of the organization to retrieve data for.
        - response (dict): The mocked JSON response expected from the API.

        Returns:
        - None
        """
        gh_org = GithubOrgClient(input)
        gh_org.org()
        ORG_URL = "https://api.github.com/orgs/{org}"
        mock_get_json.assert_called_once_with(ORG_URL.format(org=input))
