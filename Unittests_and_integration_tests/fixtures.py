#!/usr/bin/env python3
"""Fixtures for testing github org client.
"""

org_payload = {
    "login": "google",
    "id": 1342004,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
    "url": "https://api.github.com/orgs/google",
    "repos_url": "https://api.github.com/orgs/google/repos",
    "events_url": "https://api.github.com/orgs/google/events",
    "hooks_url": "https://api.github.com/orgs/google/hooks",
    "issues_url": "https://api.github.com/orgs/google/issues",
    "members_url": "https://api.github.com/orgs/google/members{/member}",
    "public_members_url": (
        "https://api.github.com/orgs/google/public_members{/member}"
    ),
    "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
    "description": "Google open source",
    "is_verified": True,
    "has_organization_projects": True,
    "has_repository_projects": True,
    "public_repos": 920,
    "public_gists": 0,
    "followers": 0,
    "following": 0,
    "html_url": "https://github.com/google",
    "created_at": "2012-01-18T01:30:18Z",
    "updated_at": "2019-11-20T21:40:48Z",
    "type": "Organization"
}

repos_payload = [
    {
        "id": 7697149,
        "node_id": "MDEwOlJlcG9zaXRvcnk3Njk7MTQ5",
        "name": "episodes.dart",
        "full_name": "google/episodes.dart",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
        },
        "html_url": "https://github.com/google/episodes.dart",
        "description": "A framework for timing performance of web apps.",
        "fork": False,
        "url": "https://api.github.com/repos/google/episodes.dart",
        "license": {
            "key": "bsd-3-clause",
            "name": "BSD 3-Clause \"New\" or \"Revised\" License",
            "spdx_id": "BSD-3-Clause",
            "url": "https://api.github.com/licenses/bsd-3-clause",
            "node_id": "MDc6TGljZW5zZTU="
        },
    },
    {
        "id": 7776515,
        "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
        "name": "cpp-netlib",
        "full_name": "google/cpp-netlib",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
        },
        "html_url": "https://github.com/google/cpp-netlib",
        "description": "The C++ Network Library Project",
        "fork": True,
        "url": "https://api.github.com/repos/google/cpp-netlib",
        "license": {
            "key": "bsl-1.0",
            "name": "Boost Software License 1.0",
            "spdx_id": "BSL-1.0",
            "url": "https://api.github.com/licenses/bsl-1.0",
            "node_id": "MDc6TGljZW5zZTI4"
        },
    },
    {
        "id": 7968417,
        "node_id": "MDEwOlJlcG9zaXRvcnk3OTY4NDE3",
        "name": "dagger",
        "full_name": "google/dagger",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
        },
        "html_url": "https://github.com/google/dagger",
        "description": "A fast dependency injector for Android and Java.",
        "fork": True,
        "url": "https://api.github.com/repos/google/dagger",
        "license": {
            "key": "apache-2.0",
            "name": "Apache License 2.0",
            "spdx_id": "Apache-2.0",
            "url": "https://api.github.com/licenses/apache-2.0",
            "node_id": "MDc6TGljZW5zZTI="
        },
    },
    {
        "id": 8165161,
        "node_id": "MDEwOlJlcG9zaXRvcnk4MTY1MTYx",
        "name": "ios-webkit-debug-proxy",
        "full_name": "google/ios-webkit-debug-proxy",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
        },
        "html_url": "https://github.com/google/ios-webkit-debug-proxy",
        "description": "A DevTools proxy for iOS devices",
        "fork": False,
        "url": "https://api.github.com/repos/google/ios-webkit-debug-proxy",
        "license": {
            "key": "other",
            "name": "Other",
            "spdx_id": "NOASSERTION",
            "url": None,
            "node_id": "MDc6TGljZW5zZTA="
        },
    },
    {
        "id": 8459994,
        "node_id": "MDEwOlJlcG9zaXRvcnk4NDU5OTk0",
        "name": "google.github.io",
        "full_name": "google/google.github.io",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
        },
        "html_url": "https://github.com/google/google.github.io",
        "description": None,
        "fork": False,
        "url": "https://api.github.com/repos/google/google.github.io",
        "license": None,
    },
    {
        "id": 8566972,
        "node_id": "MDEwOlJlcG9zaXRvcnk4NTY2OTcy",
        "name": "kratu",
        "full_name": "google/kratu",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
        },
        "html_url": "https://github.com/google/kratu",
        "description": None,
        "fork": False,
        "url": "https://api.github.com/repos/google/kratu",
        "license": {
            "key": "apache-2.0",
            "name": "Apache License 2.0",
            "spdx_id": "Apache-2.0",
            "url": "https://api.github.com/licenses/apache-2.0",
            "node_id": "MDc6TGljZW5zZTI="
        },
    },
    {
        "id": 8858648,
        "node_id": "MDEwOlJlcG9zaXRvcnk4ODU4NjQ4",
        "name": "build-debian-cloud",
        "full_name": "google/build-debian-cloud",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
        },
        "html_url": "https://github.com/google/build-debian-cloud",
        "description": "Script to create Debian Squeeze & Wheezy AMIs",
        "fork": True,
        "url": "https://api.github.com/repos/google/build-debian-cloud",
        "license": {
            "key": "other",
            "name": "Other",
            "spdx_id": "NOASSERTION",
            "url": None,
            "node_id": "MDc6TGljZW5zZTA="
        },
    },
    {
        "id": 9060347,
        "node_id": "MDEwOlJlcG9zaXRvcnk5MDYwMzQ3",
        "name": "traceur-compiler",
        "full_name": "google/traceur-compiler",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
        },
        "html_url": "https://github.com/google/traceur-compiler",
        "description": "Traceur is a JavaScript compiler",
        "fork": False,
        "url": "https://api.github.com/repos/google/traceur-compiler",
        "license": {
            "key": "apache-2.0",
            "name": "Apache License 2.0",
            "spdx_id": "Apache-2.0",
            "url": "https://api.github.com/licenses/apache-2.0",
            "node_id": "MDc6TGljZW5zZTI="
        },
    },
    {
        "id": 9065917,
        "node_id": "MDEwOlJlcG9zaXRvcnk5MDY1OTE3",
        "name": "firmata.py",
        "full_name": "google/firmata.py",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
        },
        "html_url": "https://github.com/google/firmata.py",
        "description": None,
        "fork": False,
        "url": "https://api.github.com/repos/google/firmata.py",
        "license": {
            "key": "apache-2.0",
            "name": "Apache License 2.0",
            "spdx_id": "Apache-2.0",
            "url": "https://api.github.com/licenses/apache-2.0",
            "node_id": "MDc6TGljZW5zZTI="
        },
    },
]

expected_repos = [
    "episodes.dart",
    "cpp-netlib",
    "dagger",
    "ios-webkit-debug-proxy",
    "google.github.io",
    "kratu",
    "build-debian-cloud",
    "traceur-compiler",
    "firmata.py",
]

apache2_repos = [
    "dagger",
    "kratu",
    "traceur-compiler",
    "firmata.py",
]

TEST_PAYLOAD = [
    (
        org_payload,
        repos_payload,
        expected_repos,
        apache2_repos,
    )
]
