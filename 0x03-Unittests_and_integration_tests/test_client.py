#!/usr/bin/env python3
"""Parameterized mock test for requests"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """
        Test for checking the retrieval of the public repositories URL from
        the GithubOrgClient instance.
        """
        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mock_gh_org:
            payload = {"repos_url": "google"}
            mock_gh_org.return_value = payload
            gh_org = GithubOrgClient("abc")
            resp = gh_org._public_repos_url
            self.assertEqual(resp, payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
