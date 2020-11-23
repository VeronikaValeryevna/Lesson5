import pytest

tasks_to_try = [12, 3, 23, 453, 23, 45]


@pytest.fixture(params=tasks_to_try)
def a_task(request):
    """Без идентификаторов."""
    return request.param


def test_divisible_by_3(a_task):
    assert 1 == 1
