import pytest

def pytest_configure(config):
    config.addinivalue_line("markers", "test: mark a test function")