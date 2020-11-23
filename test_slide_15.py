import pytest

param_lst = [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 21)]


@pytest.mark.parametrize("num1, num2, output", param_lst)
def test_multiplication_11(num1, num2, output):
    assert num1 * num2 == output
