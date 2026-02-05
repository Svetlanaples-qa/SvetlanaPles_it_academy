import pytest


@pytest.fixture
def data():
    data = [1, 2]
    yield data
    print("Cleanup")