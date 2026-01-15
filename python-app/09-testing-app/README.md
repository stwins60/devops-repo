# Testing Application with Pytest

Comprehensive testing suite using pytest and related tools.

## Features

- Unit tests
- Integration tests
- Fixtures and mocking
- Code coverage
- Test parameterization

## Project Structure

```
09-testing-app/
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   ├── string_utils.py
│   └── api_client.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_calculator.py
│   ├── test_string_utils.py
│   └── test_api_client.py
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_calculator.py

# Run with verbose output
pytest -v
```
