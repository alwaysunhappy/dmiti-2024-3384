import pytest
from main import *


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
def test_multiplication_by_digit(natural, number, expected):
    natural = Natural(len(natural), natural)
    result = natural.multiplication_by_digit(number)
    assert result.values == expected


@pytest.mark.parametrize("number, s_number, expected", [
    (1233, 3123, "3850659"),
    (123, 0, "0"),
    (1223433, 32134123, "39313946504259"),
    (12323, 312, "3844776"),
    (12133, 31423, "381255259"),

])
def test_mul(number, s_number, expected):
    natural = [int(i) for i in str(number)]
    s_natural = [int(i) for i in str(s_number)]
    natural = create_natural(natural)
    s_natural = create_natural(s_natural)
    result = natural.__mul__(s_natural)
    assert result.__str__() == expected


@pytest.mark.parametrize("number, s_number, expected", [
    ("-1233", "3123", "- 3850659"),
    ("123", "0", "0"),
    ("-1223433", "-32134123", "39313946504259"),
    ("12323", "-312", "- 3844776"),
    ("12133", "31423", "381255259"),

])
def test_mul_int(number, s_number, expected):
    if number[0] == "-":
        f_sign = True
        integer = [int(i) for i in number[1:]]
    else:
        f_sign = False
        integer = [int(i) for i in number]
    if s_number[0] == "-":
        s_sign = True
        s_integer = [int(i) for i in s_number[1:]]
    else:
        s_sign = False
        s_integer = [int(i) for i in s_number]
    integer = create_integer(integer, f_sign )
    s_integer = create_integer(s_integer , s_sign)
    result = integer.__mul__(s_integer)
    assert result.__str__() == expected


@pytest.mark.parametrize("number, s_number, expected", [
    ("0", "-123", "0"),
    ("123", "-123234", "0"),
    ("-1223433", "-32134123", "0"),
    ("12323", "-435", "- 28"),
    ("12132342343243432143243241234124231433", "-21431264532487231546712531232131112", "- 566"),

])
def test_quotient(number, s_number, expected):
    if number[0] == "-":
        f_sign = True
        integer = [int(i) for i in number[1:]]
    else:
        f_sign = False
        integer = [int(i) for i in number]
    if s_number[0] == "-":
        s_sign = True
        s_integer = [int(i) for i in s_number[1:]]
    else:
        s_sign = False
        s_integer = [int(i) for i in s_number]
    integer = create_integer(integer, f_sign )
    s_integer = create_integer(s_integer , s_sign)
    result = integer.quotient(s_integer)
    assert result.__str__() == expected



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


@pytest.mark.parametrize("num1, num2, number, expected", [
    (100, 9, 2, [8, 2]),
    (600, 200, 3, [0]),
    (78, 53, 0, [7, 8]),
])
def test_subtract_scaled_natural(num1, num2, number, expected):
    num1 = [int(i) for i in str(num1)]
    num2 = [int(i) for i in str(num2)]
    num1 = create_natural(num1)
    num2 = create_natural(num2)
    result = num1.subtract_scaled_natural(num2, number)
    assert result.values == expected


@pytest.mark.parametrize("num, expected_num", [
    (100, 101),
    (1, 2),
    (1234, 1235),
    (999, 1000)
])
def test_ADD_1N_N(num, expected_num):
    natural = Natural(len(str(num)), [int(i) for i in str(num)])
    natural = natural.increment()
    assert int(str(natural)) == expected_num


@pytest.mark.parametrize("num1, num2, expected", [
    ([9, 9, 9], [1], [1, 0, 0, 0]),
    ([0], [0], [0]),
    ([1, 0, 0], [1, 0], [1, 1, 0]),
    ([5, 5, 5], [5, 5, 5], [1, 1, 1, 0]),
    ([0], [1, 0], [1, 0]),
])
def test_add(num1, num2, expected):
    num1 = Natural(len(num1), num1)
    num2 = Natural(len(num2), num2)
    assert (num1 + num2).values == expected


@pytest.mark.parametrize("num1, num2, expected", [
    ([1, 0, 0, 0], [1], [9, 9, 9]),
    ([0], [0], [0]),
    ([1, 1, 0], [1, 0], [1, 0, 0]),
    ([5, 5, 5], [1, 7, 8], [3, 7, 7]),
    ([1, 0], [0], [1, 0]),
])
def test_sub(num1, num2, expected):
    num1 = Natural(len(num1), num1)
    num2 = Natural(len(num2), num2)
    assert (num1 - num2).values == expected


@pytest.mark.parametrize("num , expected", [
    (12321321321, True),
    (0000000000, False),
    (12321321, True),
    (0, False),
    (1, True),
])
def test_number_is_not_zero(num, expected):
    assert Natural(len(str(num)), [int(i) for i in str(num)]).number_is_not_zero() == expected


@pytest.mark.parametrize("num, k , expected", [
    (1232, [5], [int(i) for i in str(1232)] + [0] * 5),
    (12312, [0], [int(i) for i in str(12312)] + [0] * 0),
    (1231123232, [3], [int(i) for i in str(1231123232)] + [0] * 3),
    (0, [2], [0]),
    (12312545, [4], [int(i) for i in str(12312545)] + [0] * 4),
])
def test_multiply_by_ten(num, k, expected):
    assert Natural(len(str(num)), [int(i) for i in str(num)]).multiply_by_ten(create_natural(k)).values == expected


@pytest.mark.parametrize("num1, num2,expected", [
    (9999, 21, [4, 0, 0]),
    (456, 20, [2, 0]),
    (0, 53, [0]),
    (45456, 8765, [5]),
    (10000, 10, [1, 0, 0, 0])
])
def test_first_digit__of_scaled_division(num1, num2, expected):
    num1 = [int(i) for i in str(num1)]
    num2 = [int(i) for i in str(num2)]
    num1 = create_natural(num1)
    num2 = create_natural(num2)
    result = num1.first_digit__of_scaled_division(num2)
    assert result.values == expected


@pytest.mark.parametrize("num1, num2, expected", [
    (9999999, 21, [4, 7, 6, 1, 9, 0]),
    (145, 145, [1]),
    (34, 128, [0]),
    (7877845, 54, [1, 4, 5, 8, 8, 6]),
])
def test_div_natural(num1, num2, expected):
    num1 = [int(i) for i in str(num1)]
    num2 = [int(i) for i in str(num2)]
    num1 = create_natural(num1)
    num2 = create_natural(num2)
    result = num1.div_natural(num2)
    assert result.values == expected


@pytest.mark.parametrize("num1, num2, expected", [
    (9999999, 21, [9]),
    (145, 145, [0]),
    (34, 128, [3, 4]),
    (7877845, 54, [1]),
    (77773, 7, [3])
])
def test_mod_natural(num1, num2, expected):
    num1 = [int(i) for i in str(num1)]
    num2 = [int(i) for i in str(num2)]
    num1 = create_natural(num1)
    num2 = create_natural(num2)
    result = num1.mod_natural(num2)
    assert result.values == expected


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


@pytest.mark.parametrize("num, expected_num", [
    (-100, 100),
    (0, 0),
    (1, "- 1")
])
def test_MUL_ZM_Z(num, expected_num):
    abs_num = num * (-1) if num < 0 else num
    list_of_num = [int(i) for i in str(abs_num)]
    sign = False if num >= 0 else True
    integer = Integers(len(list_of_num), list_of_num, sign)
    integer = integer.invert_sign()
    assert str(integer) == str(expected_num)


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
    (123, 2),
    (0, 0),
    (321, 2),
    (-1000, 1),
    (-63943, 1),
])
def test_check_sign(num, expected):
    assert Integers(len(str(num)) if num >= 0 else len(str(num)) - 1, [int(i) for i in str(num) if i != '-'],
                    True if num < 0 else False).check_sign() == expected


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


@pytest.mark.parametrize("coeff, degree, k, expected_coeff", [
    (['-37/11', '53/7', '23/9'], '3', '2', ['0/1', '0/1', '- 37/11', '53/7', '23/9']),
    (['283/12', '1/3', '4/7', '2/1'], '4', '0', ['283/12', '1/3', '4/7', '2/1'])
])
def test_MUL_Pxk_P(coeff, degree, k, expected_coeff):
    rational_list = []
    for item in coeff:
        numerator = item.split('/')[0]
        denominator = item.split('/')[1]
        if numerator[0] == '-':
            sign = True
            numerator = numerator[1:]
        else:
            sign = False
        numerator = Integers(len(numerator), [int(i) for i in numerator], sign)
        rational_list += [Rational([numerator, Natural(len(denominator), [int(i) for i in denominator])])]

    polynomial = Polynomial([Natural(len(degree), [int(i) for i in degree]), rational_list])
    result = polynomial.multiply_by_monomial(Natural(len(k), [int(i) for i in k]))
    result_list = [str(i) for i in result.coefficients]
    assert result_list == expected_coeff


@pytest.mark.parametrize("natural, sign, expected, expected_exception", [
    (Natural(2, [1, 8]), True, "- 18", None),
    (Natural(2, [1, 8]), False, "18", None),
    (Natural(3, [0, 0, 5]), True, "- 005", None),
    (Natural(3, [0, 0, 5]), False, "005", None),
    (Natural(1, [0]), True, None, ValueError),
    (Natural(3, [0, 0, 0]), True, None, ValueError),
    (Natural(3, [0, 0, 0]), False, "000", None),
    (Integers(2, [1, 8], True), False, "18", None),
])
def test_trans_from_natural_in_integer(
        natural: Natural, sign: bool, expected: str, expected_exception: Exception
):
    if expected_exception:
        with pytest.raises(expected_exception):
            str(natural.trans_in_integer(sign))
    else:
        assert str(natural.trans_in_integer(sign)) == expected


@pytest.mark.parametrize("integer, expected, expected_exception", [
    (Integers(2, [1, 8], False), "18", None),
    (Integers(1, [0], False), "0", None),
    (Integers(3, [0, 0, 5], False), "005", None),
    (Integers(3, [0, 0, 0], False), "000", None),
    (Integers(2, [1, 8], True), None, ValueError),
])
def test_trans_from_integer_in_natural(
        integer: Integers, expected: str, expected_exception: Exception
):
    if expected_exception:
        with pytest.raises(expected_exception):
            str(integer.trans_in_natural())
    else:
        assert str(integer.trans_in_natural()) == expected


@pytest.mark.parametrize("integer, expected", [
    (Integers(2, [1, 8], False), "18/1"),
    (Integers(2, [1, 8], True), "- 18/1"),
    (Integers(1, [0], False), "0/1"),
    (Integers(3, [0, 0, 5], False), "005/1"),
    (Integers(3, [0, 0, 5], True), "- 005/1"),
    (Integers(3, [0, 0, 0], False), "000/1"),
])
def test_trans_from_integer_in_rational(
        integer: Integers, expected: str
):
    assert str(integer.trans_in_rational()) == expected


@pytest.mark.parametrize("rational, expected, expected_exception", [
    (Rational([Integers(2, [2, 3], False), Natural(1, [1])]), "23", None),
    (Rational([Integers(2, [2, 3], True), Natural(1, [1])]), "- 23", None),
    (Rational([Integers(1, [0], False), Natural(1, [1])]), "0", None),
    (Rational([Integers(2, [2, 3], False), Natural(1, [4])]), None, ValueError),
    (Rational([Integers(2, [2, 3], True), Natural(1, [4])]), None, ValueError),
    (Rational([Integers(2, [2, 3], False), Natural(1, [0])]), None, ValueError),
])
def test_trans_from_rational_in_integer(
        rational: Rational, expected: str, expected_exception: Exception
):
    if expected_exception:
        with pytest.raises(expected_exception):
            str(rational.trans_in_integer())
    else:
        assert str(rational.trans_in_integer()) == expected


@pytest.mark.parametrize("numerator, denominator, sign, expected_answer", [
    ([1, 2], [6], True, True),
    ([1, 0, 2], [5, 1], False, True),
    ([1, 5, 0], [4, 9], False, False)
])
def test_int_check_Rational(numerator, denominator, sign, expected_answer):
    rational = Rational([Integers(len(numerator), numerator, sign), Natural(len(denominator), denominator)])
    assert rational.int_check() == expected_answer


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


@pytest.mark.parametrize("coeff, degree, k, expected_coeff", [
    (['-37/11', '53/7', '23/9'], '3', '2', ['53/7', '46/9']),
    (['283/12', '1/3', '4/7', '2/1'], '4', '0', ['1/3', '8/7', '6/1'])
])
def test_div_pol(coeff, degree, k, expected_coeff):
    rational_list = []
    for item in coeff:
        numerator = item.split('/')[0]
        denominator = item.split('/')[1]
        if numerator[0] == '-':
            sign = True
            numerator = numerator[1:]
        else:
            sign = False
        numerator = Integers(len(numerator), [int(i) for i in numerator], sign)
        rational_list += [Rational([numerator, Natural(len(denominator), [int(i) for i in denominator])])]

    polynomial = Polynomial([Natural(len(degree), [int(i) for i in degree]), rational_list])
    result = list(map(str, polynomial.pol_derivative().coefficients))
    assert result == expected_coeff


@pytest.mark.parametrize("num1, num2, expected_nod", [
    ([9, 9, 9, 9], [2, 1], [3]),
    ([4, 5, 6], [2, 0], [4]),
    ([4, 5, 4, 5, 6], [8, 7, 6, 5], [1]),
    ([1, 0, 0], [2, 0], [2, 0])
])
def test_gcd_natural(num1, num2, expected_nod):
    num1 = create_natural(num1)
    num2 = create_natural(num2)

    result = num1.gcf_natural(num2)
    assert result.values == expected_nod


@pytest.mark.parametrize("num1, num2, expected_nod", [
    ([1, 8], [4, 8], [1, 4, 4]),
    ([4], [5, 5], [2, 2, 0])
])
def test_lmc_natural(num1, num2, expected_nod):
    num1 = create_natural(num1)
    num2 = create_natural(num2)

    result = num1.lmc_natural(num2)
    assert result.values == expected_nod
