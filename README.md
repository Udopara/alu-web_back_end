# Unittests and Integration Tests

This repository contains the implementation and test suites for the **Unittests and Integration Tests** project of the ALU Web Back End curriculum.

## Overview

The project demonstrates key Python testing patterns, including:
- Unit testing with `unittest.TestCase`
- Parametrization with `@parameterized.expand` and `@parameterized_class`
- Mocking external HTTP requests and functions with `unittest.mock.patch`, `Mock`, and `PropertyMock`
- Testing decorator behaviors (such as `@memoize`)
- Integration testing using static fixture data

## Directory Structure

```
Unittests_and_integration_tests/
├── client.py        # GithubOrgClient implementation
├── utils.py         # Utility functions (access_nested_map, get_json, memoize)
├── fixtures.py      # Sample fixture data for integration tests
├── test_utils.py    # Unit tests for utils.py
└── test_client.py   # Unit and integration tests for client.py
```

## Running the Tests

To run the complete test suite:

```bash
PYTHONPATH=Unittests_and_integration_tests python3 -m unittest discover -s Unittests_and_integration_tests -p "test_*.py"
```

To run individual test files:

```bash
PYTHONPATH=Unittests_and_integration_tests python3 -m unittest Unittests_and_integration_tests/test_utils.py
PYTHONPATH=Unittests_and_integration_tests python3 -m unittest Unittests_and_integration_tests/test_client.py
```

## Code Style

All Python files conform to the `pycodestyle` standard (version 2.5):

```bash
pycodestyle Unittests_and_integration_tests/*.py
```