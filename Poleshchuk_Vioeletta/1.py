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

    def check_leader_zero(self):
        self.values.reverse()
        while self.n > 1 and self.values[self.n - 1] == 0:
            self.values.pop()
            self.n -= 1
        self.values.reverse()

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
        natural = Natural(len(answer), answer)
        natural.check_leader_zero()
        return natural
    
    def increment(self):
        shift = 1  # Начальное значение для переноса (мы добавляем 1)
        for index in range(self.n - 1, -1, -1):
            self.values[index] += shift  # Добавляем перенос к текущей цифре
            if self.values[index] < 10:
                shift = 0  # Если нет переноса, выходим из цикла
                break
            else:
                self.values[index] = 0  # Устанавливаем 0, если есть перенос
                shift = 1  # Перенос на следующий разряд

        # Если по завершении цикла все разряды переноса заполнены, добавляем 1 в старший разряд
        if shift == 1:
            self.values.insert(0, 1)
            self.n += 1  # Увеличиваем длину числа на 1

        return self

 


# (n; values[..], sign) - (длина числа, массив цивр, знак)
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
        if self.sign is True:  # проверяем знак
            self.sign = False  # если знак числа минус, то меняем знак на положительный
        return self  # выводим получившиеся число


# массив пар (целое; натуральное), первое имеет смысл числителя, второе - знаменателя
class Rational:
    def __init__(self, array_rational: list[Integers, Natural]):
        self.numerator = array_rational[0]  # числитель дроби
        self.denominator = array_rational[1]  # знаменатель дроби


# массив пар (degree – степень многочлена и массив C коэффициентов)
class Polynomial:
    def __init__(self, array_polynomial: list[Natural, list[Rational]]):
        self.degree = array_polynomial[0]  # степень первого многочлена
        self.coefficients = array_polynomial[1]  # коэффиценты первого многочлена

    def degree_polynomial(self):
        """
        DEG_P_N
        Функция возвращает степень многочлена
        """
        return self.degree  # возвращает степень многочлена


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
    new_degrees = []
    polynomial = input_polynomial()
    degrees = polynomial[1]
    coefficients = polynomial[0]
    max_degree = polynomial[2]
    for degree in range(max_degree + 1):
        new_degrees.append(degree)
    new_coefficients = [Rational([Integers(1, [0], False), Natural(1, [1])])] * len(new_degrees)
    for i, degree in enumerate(degrees):
        index = 0
        for k in range(len(new_degrees)):
            if int("".join(list(map(str, degree.values)))) == new_degrees[k]:
                index = k
                break
        new_coefficients[index] = coefficients[i]
    max_degree = [int(i) for i in str(max_degree)]
    return Polynomial([Natural(len(max_degree), max_degree), new_coefficients])


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
            print("".join([str(i) for i in natural.__add__(natural_second).values]))
        if self.number == 15:
            integers = input_integer()
            print("".join([str(i) for i in integers.abs_integer().values]))
        if self.number == 38:
            polynomial = create_polynomial()
            print("".join([str(i) for i in polynomial.degree_polynomial().values]))


if __name__ == "__main__":
    number = Natural(10, [2, 3, 9, 8, 9, 8, 9, 9, 9, 8])
    print(number.increment().values)