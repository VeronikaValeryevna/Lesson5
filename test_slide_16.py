import pytest


@pytest.mark.xfail
def test_1():
    num = 100
    assert num > 100


@pytest.mark.xfail
def test_2():
    num = 100
    assert num >= 100


@pytest.mark.skip
def test_3():
    num = 100
    assert num < 200
