# (n; values[..]) - номер старшей позиции и массив цифр
class Natural:
    def __init__(self, n: int, values: list[int]):
        self.n = n  # длина массива
        self.values = values  # массив натуралных чисел

    def cmp_of_natural_number(self):
        """
         Сравнивает два натуральных числа и возвращает:
          2 - если первое число больше второго,
          0 - если числа равны,
          1 - если первое число меньше второго.
        """
        str_values = [str(self.values[0]), str(self.values[1])]
        if len(str_values[0]) > len(str_values[1]):
            return 2
        elif len(str_values[0]) < len(str_values[1]):
            return 1
        else:
            for i in range(len(str_values[0]) - 1, -1, -1):
                if str_values[0][i] > str_values[1][i]:
                    return 2
                elif str_values[0][i] < str_values[1][i]:
                    return 1
        return 0


# (n; values[..], sign) - знак числа (1 — минус, 0 — плюс) номер старшей позиции и массив цифр
class Integers:
    def __init__(self, n: int, values: list[int], sign=False):
        self.sign = sign  # знак первого числа, если True, то минус
        self.n = n  # длина массива
        self.values = values  # массив целых чисел
        if self.sign:
            values[0] = -values[0]  # поменяли знак у первого числа


# массив пар (целое; натуральное), первое имеет смысл числителя, второе - знаменателя
class Rational:
    def __init__(self, array_rational: list[list]):
        self.numerator_first = array_rational[0][0]  # числитель первой дроби
        self.denominator_first = array_rational[0][1]  # знаменатель первой дроби
        if len(array_rational) == 2:
            self.numerator_second = array_rational[1][0]  # числитель второй дроби
            self.denominator_second = array_rational[1][1]  # знаменатель второй дроби


# массив пар (degree – степень многочлена и массив C коэффициентов)
class Polynomial:
    def __init__(self, array_polynomial: list[list]):
        self.degree_first = array_polynomial[0][0]  # степень первого многочлена
        self.coefficients_first = array_polynomial[0][1]  # коэффиценты первого многочлена
        if len(array_polynomial) == 2:
            self.degree_second = array_polynomial[1][0]  # степень второго многочлена
            self.coefficients_second = array_polynomial[1][1]  # коэффиценты второго многочлена
            print(self.coefficients_second, self.degree_second)


def input_natural():
    print("Введите натуральые числа через пробел:")
    array = list(map(int, input().split()))
    return Natural(len(array), array)


def input_integer():
    sign = bool(input("Введите знак числа (1 - отрицательное, 0 положительное)"))
    print("Введите целые числа через пробел:")
    array = list(map(int, input().split()))
    return Integers(len(array), array, sign)


def input_rational():
    print("Введите числитель и знаменатель через пробле: ")
    array = list(map(int, input().split()))
    return array


def create_rational(quantity: int):
    if quantity == 1:
        return Rational([input_rational()])
    else:
        return Rational([input_rational(), input_rational()])


def input_polynomial():
    print("Введите многочлен в формате коэффицент степень коэффицент степень ... :")
    array = list(map(int, input().split()))
    coefficient = [array[i] for i in range(0, len(array), 2)]
    degree = [array[i] for i in range(1, len(array), 2)]
    return coefficient, degree


def create_polynomial(quantity: int):
    array_coef = []
    for j in range(quantity):
        new_degrees = []
        polynomial = input_polynomial()
        degrees = polynomial[1]
        coefficients = polynomial[0]
        for degree in range(max(degrees), -1, -1):
            new_degrees.append(degree)
        new_coefficients = [0] * len(new_degrees)
        for i, degree in enumerate(degrees):
            index = new_degrees.index(degree)
            new_coefficients[index] = coefficients[i]
        array_coef.append(new_coefficients)
    if quantity == 1:
        Polynomial([[len(array_coef[0]) - 1, array_coef[0]]])
    else:
        return Polynomial([[len(array_coef[0]) - 1, array_coef[0]], [len(array_coef[1]) - 1, array_coef[1]]])


class Launch:
    def __init__(self, number):
        self.number = number

    def start_function(self):
        if self.number == 1:
            natural = input_natural()
            print(natural.cmp_of_natural_number())


if __name__ == "__main__":
    Launch(1).start_function()