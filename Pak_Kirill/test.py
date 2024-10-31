from main import Natural
import pytest


@pytest.mark.parametrize("num , expected", [
    (12321321321 , True),
    (0000000000 , False),
    (12321321 , True),
    (0 , False),
    (1 , True),
])
def test_number_is_not_zero(num, expected):
    assert Natural(len(str(num)) , [int(i) for i in str(num)]).number_is_not_zero() == expected

@pytest.mark.parametrize("num, k , expected", [
    (1232, 5, [int(i) for i in str(1232)] + [0]*5),
    (12312, 0, [int(i) for i in str(12312)] + [0]*0),
    (1231123232, 3, [int(i) for i in str(1231123232)] + [0]*3),
    (0, 2, [0]),
    (12312545, 4, [int(i) for i in str(12312545)] + [0]*4),
])
def test_multiply_by_ten(num, k , expected):
    assert Natural(len(str(num)) , [int(i) for i in str(num)]).multiply_by_ten(k).values == expected