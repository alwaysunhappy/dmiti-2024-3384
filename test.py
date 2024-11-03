from main import *
import pytest


@pytest.mark.parametrize("num, expected_n, expected_values", [
    (100, 3, [1, 0, 0]),
    (0, 1, [0]),
    (1234, 4, [1, 2, 3, 4]),
])
def test_Natural(num, expected_n, expected_values):
    num = [int(i) for i in str(num)]
    natural = Natural(len(num), num)
    assert natural.values == expected_values and natural.n == expected_n


@pytest.mark.parametrize("num, expected", [
    (100, ValueError),
    (0, ValueError),
    (1234, ValueError),
])
def test_Natural_ValueError(num, expected):
    num = [int(i) for i in str(num)]
    with pytest.raises(expected):
        natural = Natural(len(num) + 1, num)


@pytest.mark.parametrize("natural, number, expected", [
    ([9, 9, 9], 9, [8, 9, 9, 1]),
    ([9, 9, 9], 0, [0]),
    ([5], 5, [2, 5]),
    ([9, 9, 9], 1, [9, 9, 9])
])
def test_mul(natural, number, expected):
    natural = Natural(len(natural), natural)
    result = natural.__mul__(number)
    assert result.values == expected

    
@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 2),
    (10, 10, 0),
    (2, 7, 1),
    (0, 1, 1),
    (100, 50, 2),
])
def test_cmp_of_natural_number(num1, num2, expected):
    num1 = [int(i) for i in str(num1)]
    num2 = [int(i) for i in str(num2)]
    num1 = create_natural(num1)
    num2 = create_natural(num2)
    assert num1.cmp_of_natural_number(num2) == expected


@pytest.mark.parametrize("num, sign, expected_n, expected_values, expected_sign", [
    (100, False, 3, [1, 0, 0], False),
    (0, False, 1, [0], False),
    (1234, False, 4, [1, 2, 3, 4], False),
    (100, True, 3, [1, 0, 0], True),
    (1234, True, 4, [1, 2, 3, 4], True),
])
def test_Integers(num, sign, expected_n, expected_values, expected_sign):
    num = [int(i) for i in str(num)]
    integer = Integers(len(num), num, sign)
    assert integer.values == expected_values and integer.n == expected_n and integer.sign == expected_sign


@pytest.mark.parametrize("num, expected", [
    (-1, [1]),
    (10, [1, 0]),
    (0, [0]),
    (-999, [9, 9, 9]),
    (999, [9, 9, 9]),
])
def test_abs_integer(num, expected):
    str_num1 = str(num)
    if str_num1[0] == '-':
        sign = True
        str_num1 = str_num1[1:]
    else:
        sign = False
    num = [int(i) for i in str_num1]
    integers = create_integer(num, sign)
    assert integers.abs_integer().values == expected


@pytest.mark.parametrize("numerator, denominator, sign, expected_numerator_n, expected_numerator_values, "
                         "expected_denominator_n, expected_denominator_values", [
                             ([1, 0, 0], [1, 0], True, 3, [1, 0, 0], 2, [1, 0]),
                             ([0], [1], False, 1, [0], 1, [1]),
                             ([1, 2, 3, 4], [5, 6, 7, 8], False, 4, [1, 2, 3, 4], 4, [5, 6, 7, 8]),
                             ([1, 0, 0], [1, 0], True, 3, [1, 0, 0], 2, [1, 0]),
                             ([1, 2, 3, 4], [5, 6, 7, 8], True, 4, [1, 2, 3, 4], 4, [5, 6, 7, 8]),
                         ])
def test_Rational(numerator, denominator, sign, expected_numerator_n, expected_numerator_values, expected_denominator_n,
                  expected_denominator_values):
    rational = Rational([Integers(len(numerator), numerator, sign), Natural(len(denominator), denominator)])
    assert rational.numerator.values == expected_numerator_values and rational.numerator.n == expected_numerator_n
    assert rational.denominator.values == expected_denominator_values and rational.denominator.n == expected_denominator_n

  
@pytest.mark.parametrize("num , expected", [
    (123 , 2),
    (0, 0),
    (321 , 2),
    (-1000 , 1),
    (-63943 , 1),
])
def test_check_sign(num, expected):
    assert Integers(len(str(num)) if num>=0 else len(str(num))-1 , [int(i) for i in str(num) if i!= '-'] , True if num<0 else False).check_sign() == expected


@pytest.mark.parametrize("degree, array_coef, expected", [
    (5, [[0], [1], [2], [3], [4], [5]], 5),
    (2, [[0], [0], [1, 0, 0, 0]], 2),
    (0, [[1, 0]], 0),
])
def test_degree_polynomial(degree, array_coef, expected):
    denominator = create_natural([1])
    degree = [int(i) for i in str(degree)]
    degree = create_natural(degree)
    new_coefficients = [Rational([Integers(1, [0], False), Natural(1, [1])])] * len(array_coef)
    for i in range(len(array_coef)):
        array_coef[i] = create_integer(array_coef[i], False)
        new_coefficients[i] = create_rational(array_coef[i], denominator)
    assert Polynomial([degree, new_coefficients]).degree_polynomial().values == [expected]
    
@pytest.mark.parametrize("num1, num2, expected_values, expected_sign", [
    (50, 25, [2, 5], False),    
    (25, 50, [2, 5], True),    
    (-50, -25, [2, 5], True),  
    (-25, -50, [2, 5], False),  
    (50, -25, [7, 5], False),   
    (-25, 50, [7, 5], True),   
    (25, 25, [0], False),     
    (-25, -25, [0], False),    
    (0, 50, [5, 0], True),      
    (50, 0, [5, 0], False),     
    (0, 0, [0], False) 
])
def test_subtraction_integers(num1, num2, expected_values, expected_sign):

    num1_obj = Integers(len(str(abs(num1))), [int(i) for i in str(abs(num1))], num1 < 0)
    num2_obj = Integers(len(str(abs(num2))), [int(i) for i in str(abs(num2))], num2 < 0)

    result = num1_obj.subtraction_integers(num2_obj)
    
    assert result.values == expected_values
    assert result.sign == expected_sign

