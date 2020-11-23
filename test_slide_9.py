import pytest


@pytest.fixture()
def fixture_1():
    print("первая фикстура")


@pytest.fixture()
def fixture_2(fixture_1):
    print("вторая фикстура")
