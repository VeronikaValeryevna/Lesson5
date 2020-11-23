import math


def test_1():
    num = 25
    assert math.sqrt(num) == 5


def test_2():
    lst = [12, 4, 23, 5]
    assert max(lst) == 23


def test_3():
    lst = [12, 4, 23, 5]
    assert max(lst) == 24
