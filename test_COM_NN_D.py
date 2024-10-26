from main import COM_NN_D
import pytest


@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 2),
    (10, 10, 0),
    (2, 7, 1),
    (0, 1, 1),
    (100, 50, 2),
])
def test_COM_NN_D(num1, num2, expected):
    assert COM_NN_D(num1, num2) == expected
