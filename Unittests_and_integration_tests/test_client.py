#!/usr/bin/env python3
"""Unit and integration tests for client module.
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from typing import Dict, List
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Unit test suite for GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json: MagicMock) -> None:
        """Test GithubOrgClient.org returns correct payload.
        """
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self) -> None:
        """Test GithubOrgClient._public_repos_url returns expected url.
        """
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
            client = GithubOrgClient("google")
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Test GithubOrgClient.public_repos returns list of repo names.
        """
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload
        with patch.object(
            GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
        self, repo: Dict[str, Dict], license_key: str, expected: bool
    ) -> None:
        """Test GithubOrgClient.has_license returns correct boolean value.
        """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test suite for GithubOrgClient using fixtures.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """Set up integration test class fixture by patching requests.get.
        """
        route_payload = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        def get_payload(url: str):
            mock_resp = Mock()
            if url in route_payload:
                mock_resp.json.return_value = route_payload[url]
            else:
                mock_resp.json.return_value = {}
            return mock_resp

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Clean up class patcher after integration tests.
        """
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Integration test for GithubOrgClient.public_repos.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Integration test for GithubOrgClient.public_repos with license.
        """
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos("apache-2.0"), self.apache2_repos
        )
