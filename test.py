from main import Natural
import pytest


@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 2),
    (10, 10, 0),
    (2, 7, 1),
    (0, 1, 1),
    (100, 50, 2),
])
def test_cmp_of_natural_number(num1, num2, expected):
    assert Natural(2, [num1, num2]).cmp_of_natural_number() == expected
