from python_tools.src.multi import MultiType, multiplex

import pytest


def addition(i: int) -> int:
    return i + 1


@pytest.mark.parametrize("multi_type", [MultiType.threading, MultiType.processing])
def test_multiplex(multi_type):
    test_list = list(range(0, 200))

    result = multiplex(addition, test_list, multi_type)
    assert list(range(1, 201)) == list(result)
