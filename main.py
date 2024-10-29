# (n; values[..]) - номер старшей позиции и массив цифр
class Natural:
    def __init__(self, n: list[int], values: list[list]):
        self.n_first = n[0]  # длина первого массива
        self.values_first = values[0]  # массив цифр первого натурального числа
        if len(n) == 2:
            self.n_second = n[1]  # длина второго массива
            self.values_second = values[1]  # массив цифр второго натурального числа

    def cmp_of_natural_number(self):
        """
         Сравнивает два натуральных числа и возвращает:
          2 - если первое число больше второго,
          0 - если числа равны,
          1 - если первое число меньше второго.
        """
        if self.n_first > self.n_second:
            return 2
        elif self.n_first < self.n_second:
            return 1
        else:
            for i in range(self.n_first - 1, -1, -1):
                if self.values_first[i] > self.values_second[i]:
                    return 2
                elif self.values_first[i] < self.values_second[i]:
                    return 1
        return 0

    def addition_of_natural(self):
        """
        ADD_NN_N
        Складывает два натурльынх числа и возвращает результат
        """
        shift = 0  # перенос в следущий разряд
        if self.cmp_of_natural_number() == 2 or self.cmp_of_natural_number() == 0:  # если первое число больше или равно
            answer = [0] * (self.n_first + 1)  # загатавливаем под ответ массив длиной на один разряд больше
            for i in range(1, self.n_first + 2):  # перебираем так, чтобы идти с конца числа -1 индекс, -2 индекс и т.д.
                if self.n_second >= i:  # если у второго числа еще есть, что складывать
                    total = self.values_first[-i] + self.values_second[-i] + shift  # складываем две цифры и перенос
                    answer[-i] = total % 10  # получаем цифру которая запишется в этом разряде
                    shift = total // 10  # считаем перенос на след разряд
                elif self.n_first >= i:  # когда у второго числа уже нечего складывать
                    total = self.values_first[-i] + shift
                    answer[-i] = total % 10
                    shift = total // 10
                else:
                    answer[-i] = shift  # обрабатываем случай, если перенос случился на первом разрде (9 + 99 = 18)
                    # <- здесь запишем единицу
        else:
            answer = [0] * (self.n_second + 1)
            for i in range(1, self.n_second + 2):
                if self.n_first >= i:
                    total = self.values_first[-i] + self.values_second[-i] + shift
                    answer[-i] = total % 10
                    shift = total // 10
                elif self.n_second >= i:
                    total = self.values_second[-i] + shift
                    answer[-i] = total % 10
                    shift = total // 10
                else:
                    answer[-i] = shift
        answer = list(map(str, answer))
        return int("".join(answer)) if answer[0] != 0 else int("".join(answer[1:]))


# (n; values[..], sign) - [[длины чисел], [сами числа в виде массивов(каждое число отдельный массив)], [знак числа]]
class Integers:
    def __init__(self, n: list[int], values: list[list], sign: list[bool]):
        self.sign_first = sign[0]  # знак первого числа, если True, то минус
        self.n_first = n[0]  # длина  первого массива
        self.values_first = values[0]  # первое целое число
        if len(n) == 2:
            self.sign_second = sign[1]  # знак второго числа
            self.n_second = n[1]  # длина второго массива
            self.values_second = values[1]  # второе целое число

    def abs_integer(self):
        """

            ABS_Z_N
            Функция берет модуль числа и возвращает его

        """
        values = list(map(str, self.values_first))  # делаем массив числа строковым типом
        if self.sign_first is True:  # проверяем знак
            self.sign_first = False  # если знак числа минус, то меняем знак на положительный
        return int(''.join(values))  # выводим получившиеся число


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

    def degree_polynomial(self):
        """

            Функция возвращает степень многочлена

        """
        return self.degree_first  # возвращает степень многочлена


def input_natural():
    print("Введите натуральое число:", end=' ')
    array = [int(i) for i in input()]
    return array


def create_natural(quantity: int):
    if quantity == 1:
        array = input_natural()
        return Natural([len(array)], [array])
    else:
        array_1 = input_natural()
        array_2 = input_natural()
        return Natural([len(array_1), len(array_2)], [array_1, array_2])


def input_integer():
    sign = bool(input("Введите знак числа (1 - отрицательное, 0 положительное): "))
    print("Введите целое число:", end=' ')
    array = [int(i) for i in input()]
    return array, sign


def create_integer(quantity: int):
    if quantity == 1:
        array, sign = input_integer()
        return Integers([len(array)], [array], [sign])
    else:
        array_first, sign_first = input_integer()
        array_second, sign_second = input_integer()
        return Integers([len(array_first), len(array_second)], [array_first, array_second], [sign_first, sign_second])


def input_rational():
    print("Введите числитель и знаменатель через пробле: ", end=' ')
    array = list(map(int, input().split()))
    return array


def create_rational(quantity: int):
    if quantity == 1:
        return Rational([input_rational()])
    else:
        return Rational([input_rational(), input_rational()])


def input_polynomial():
    print("Введите многочлен в формате коэффицент степень коэффицент степень ... :", end=' ')
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
        return Polynomial([[len(array_coef[0]) - 1, array_coef[0]]])
    else:
        return Polynomial([[len(array_coef[0]) - 1, array_coef[0]], [len(array_coef[1]) - 1, array_coef[1]]])


class Launch:
    def __init__(self, number):
        self.number = number

    def start_function(self):
        if self.number == 1:
            natural = create_natural(2)
            print(natural.cmp_of_natural_number())
        if self.number == 4:
            natural = create_natural(2)
            print(natural.addition_of_natural())
        if self.number == 15:
            integers = create_integer(1)
            print(integers.abs_integer())
        if self.number == 38:
            polynomial = create_polynomial(1)
            print(polynomial.degree_polynomial())


if __name__ == "__main__":
    Launch(...).start_function()
