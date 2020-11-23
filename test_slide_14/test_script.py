import pytest


def test_1():
    n = 101
    assert n < 120, "Это число должно быть меньше 120"
    assert n % 2 == 0, "Это число должно быть четным"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
