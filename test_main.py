# (n; values[..]) - номер старшей позиции и массив цифр
class Natural:
    def __init__(self, n: int, values: list[int]):
        self.n = n  # длина  массива
        self.values = values  # массив цифр  натурального числа

    def cmp_of_natural_number(self, other):
        """
         Сравнивает два натуральных числа и возвращает:
          2 - если первое число больше второго,
          0 - если числа равны,
          1 - если первое число меньше второго.
        """
        if self.n > other.n:
            return 2
        elif self.n < other.n:
            return 1
        else:
            for i in range(self.n - 1, -1, -1):
                if self.values[i] > other.values[i]:
                    return 2
                elif self.values[i] < other.values[i]:
                    return 1
        return 0

    def __add__(self, other):  # сложение двух натуральных чисел
        """
        ADD_NN_N
        Складывает два натурльынх числа и возвращает результат
        """
        shift = 0  # перенос в следущий разряд
        if self.cmp_of_natural_number(other) == 2 or self.cmp_of_natural_number(other) == 0:
            answer = [0] * (self.n + 1)  # загатавливаем под ответ массив длиной на один разряд больше
            for i in range(1, self.n + 2):  # перебираем -1 индекс,-2 индекс и т.д.
                if other.n >= i:  # если у второго числа еще есть, что складывать
                    total = self.values[-i] + other.values[-i] + shift
                    answer[-i] = total % 10  # получаем цифру которая запишется в этом разряде
                    shift = total // 10  # считаем перенос на след разряд
                elif self.n >= i:  # когда у второго числа уже нечего складывать
                    total = self.values[-i] + shift
                    answer[-i] = total % 10
                    shift = total // 10
                else:
                    answer[-i] = shift  # обрабатываем случай, если перенос случился на первом разрде (9 + 99 = 18)
                    # <- здесь запишем единицу
        else:
            answer = [0] * (other.n + 1)
            for i in range(1, other.n + 2):
                if self.n >= i:
                    total = self.values[-i] + other.values[-i] + shift
                    answer[-i] = total % 10
                    shift = total // 10
                elif other.n >= i:
                    total = other.values[-i] + shift
                    answer[-i] = total % 10
                    shift = total // 10
                else:
                    answer[-i] = shift
        answer = list(map(str, answer))
        return int("".join(answer)) if answer[0] != 0 else int("".join(answer[1:]))


# (n; values[..], sign) - [[длины чисел], [сами числа в виде массивов(каждое число отдельный массив)], [знак числа]]
class Integers:
    def __init__(self, n: int, values: list[int], sign: bool):
        self.sign = sign  # знак числа, если True, то минус
        self.n = n  # длина массива
        self.values = values  # первое число

    def abs_integer(self):
        """
            ABS_Z_N
            Функция берет модуль числа и возвращает его

        """
        values = list(map(str, self.values))  # делаем массив числа строковым типом
        if self.sign is True:  # проверяем знак
            self.sign = False  # если знак числа минус, то меняем знак на положительный
        return int(''.join(values))  # выводим получившиеся число


# массив пар (целое; натуральное), первое имеет смысл числителя, второе - знаменателя
class Rational:
    def __init__(self, array_rational: list[Integers, Natural]):
        self.numerator = array_rational[0]  # числитель дроби
        self.denominator = array_rational[1]  # знаменатель дроби


# массив пар (degree – степень многочлена и массив C коэффициентов)
class Polynomial:
    def __init__(self, array_polynomial: list[Natural, list[Rational]]):
        self.degree = array_polynomial[0]  # степень первого многочлена
        self.coefficients = array_polynomial[0]  # коэффиценты первого многочлена

    def degree_polynomial(self):
        """
        DEG_P_N
        Функция возвращает степень многочлена
        """
        return "".join(map(str, self.degree.values))  # возвращает степень многочлена


def input_natural():
    print("Введите натуральое число:", end=' ')
    array = [int(i) for i in input()]
    return create_natural(array)


def create_natural(array):
    return Natural(len(array), array)


def input_integer():
    print("Введите целое число:", end=' ')
    array = input()
    if array[0] == '-':
        sign = True
        array = array[1:]
    else:
        sign = False
    array = [int(i) for i in array]
    return create_integer(array, sign)


def create_integer(array, sign):
    return Integers(len(array), array, sign)


def input_rational():
    print("Введите дробь в формате x/y, где числитель - целое, знаменатель натуралньое.")
    numerator, denominator = input().split('/')
    if numerator[0] == '-':
        sign = True
        numerator = numerator[1:]
    else:
        sign = False
    numerator = [int(i) for i in numerator]
    denominator = [int(i) for i in denominator]
    return create_rational(create_integer(numerator, sign), create_natural(denominator))


def create_rational(numerator, denominator):
    return Rational([numerator, denominator])


def input_polynomial():
    coefficients = []
    degrees = []
    max_degree = 0
    while True:
        term = input("Введите член многочлена вида 3/4x^2(или 'стоп' для завершения): ")
        if term.lower() != 'стоп':
            parts = term.split('x^')
            degree = parts[1]
            max_degree = max(int(degree), max_degree)
            numerator, denominator = parts[0].split('/')
            if numerator[0] == '-':
                sign = True
                numerator = numerator[1:]
            else:
                sign = False
            numerator = [int(i) for i in numerator]
            denominator = [int(i) for i in denominator]
            degree = [int(i) for i in degree]
            coefficients.append(create_rational(create_integer(numerator, sign), create_natural(denominator)))
            degrees.append(create_natural(degree))
        else:
            break
    return coefficients, degrees, max_degree


def create_polynomial():
    array_coef = []
    new_degrees = []
    polynomial = input_polynomial()
    degrees = polynomial[1]
    coefficients = polynomial[0]
    max_degree = polynomial[2]
    for degree in range(max_degree, -1, -1):
        new_degrees.append(degree)
    new_coefficients = [coefficients[0]] * len(new_degrees)
    for i, degree in enumerate(degrees):
        index = 0
        for k in range(len(degrees)):
            if degree == degrees[k]:
                index = k
                break
        new_coefficients[index] = coefficients[i]
    array_coef.append(new_coefficients)
    max_degree = [int(i) for i in str(max_degree)]
    return Polynomial([Natural(len(max_degree), max_degree), array_coef])


class Launch:
    def __init__(self, number):
        self.number = number

    def start_function(self):
        if self.number == 1:
            natural = input_natural()
            natural_second = input_natural()
            print(natural.cmp_of_natural_number(natural_second))
        if self.number == 4:
            natural = input_natural()
            natural_second = input_natural()
            print(natural.__add__(natural_second))
        if self.number == 15:
            integers = input_integer()
            print(integers.abs_integer())
        if self.number == 38:
            polynomial = create_polynomial()
            print(polynomial.degree_polynomial())


if __name__ == "__main__":
    Launch(38).start_function()

