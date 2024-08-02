#!/usr/bin/env python3
"""Parameterized mock test for requests"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient

ORG_URL = "https://api.github.com/orgs/{org}"


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org, response, mock_get_json):
        """
        Test case to validate the GithubOrgClient class for fetching
        organization data.

        Parameters:
        - org (str): The name of the organization to retrieve data for.
        - response (dict): The mocked JSON response expected from the API.

        Returns:
        - None
        """
        mock_get_json.return_value = Mock(return_value=response)
        gh_org = GithubOrgClient(org)
        self.assertEqual(gh_org.org(), response)
        mock_get_json.assert_called_once_with(ORG_URL.format(org=org))


if __name__ == "__main__":
    unittest.main()
