class Natural:
    """
        Представляет натуральное число, хранящееся в виде массива цифр.

        Attributes:
            n: Длина массива, представляющего натуральное число.
            values: Массив цифр натурального числа.
    """
    def __init__(self, n: int, values: list[int]):
        if n != len(values) or n == 0 or len(values) == 0:
            raise ValueError("Неправильная длина числа!")
        else:
            self.n = n  # длина  массива
        self.values = values  # массив цифр  натурального числа

    def del_leader_zero(self):
        """
            Удаление незначимого 0 в начале.
        """
        while self.n > 1 and self.values[0] == 0:
            self.values.pop(0)
            self.n -= 1

    def copy(self):
        """
            Копирование натуралного числа.
        """
        return Natural(self.n, self.values.copy())

    def __mul__(self, number):
        """
            MUL_ND_N
            Умножение натурального числа на цифру
        """
        answer = [0] * (self.n + 1) # Создаем список нулей длиной n + 1 для хранения результата
        shift = 0  # перенос в следующий разряд
        for i in range(1, self.n + 2):
            # Если индекс разряда i меньше или равен длине натурального числа
            if self.n >= i:
                # Вычисляем произведение значения разряда i на цифру, добавляя перенос
                total = self.values[-i] * number + shift
                answer[-i] = total % 10
                shift = total // 10
            else:
                # Если индекс i превышает длину натурального числа, в результат просто записываем перенос
                answer[-i] = shift
        natural = Natural(len(answer), answer)
        natural.del_leader_zero()
        return natural

    def cmp_of_natural_number(self, other):
        """
            Сравнивает два натуральных числа и возвращает:
            2 - если первое число больше второго,
            0 - если числа равны,
            1 - если первое число меньше второго.
        """
        if self.n > other.n:  # проверяем, больше ли длина первого числа длины второго, что означает, что первое больше
            return 2
        elif self.n < other.n:  # иначе, больше второе число
            return 1
        else:  # если их длины равны, проверяем числа, начиная с нулевого разряда
            for i in range(self.n):
                if self.values[i] > other.values[i]:
                    return 2
                elif self.values[i] < other.values[i]:
                    return 1
        return 0
    
    def __str__(self):
        return "".join(list(map(str, self.values)))


class Integers(Natural):
    """
    Класс, представляющий целые числа.

    Наследует от класса Natural, который  представляет натуральные числа.

    Атрибуты:
      n: Целое число, которое представляет объект.
      values: Список цифр, составляющих целое число. Может возникнуть ситуация, когда первой цифрой будет 0.
      sign: Булевый флаг, указывающий знак числа.
         True - отрицательное число, False - положительное.
    """
    def __init__(self, n: int, values: list[int], sign: bool):
        super().__init__(n, values)
        self.sign = sign  # знак числа, если True, то минус
        
    def check_sign(self):
        """
        POZ_Z_D
        Определение положительности числа. (0-число равно 0, 1 - отрицательное, 2 - положительное)
        """
        if (self.n == 1 and self.values[0]==0): # Проверяем, является ли число нулем
            return 0
        else:
            if not(self.sign): # Проверем отрицательное (sign = true) число или нет
                return 2
            return 1

    def abs_integer(self):
        """
            ABS_Z_N
            Функция берет модуль числа и возвращает его
        """
        if self.sign is True:  # проверяем знак
            self.sign = False  # если знак числа минус, то меняем знак на положительный
        return self  # выводим получившиеся число

    def __str__(self):
        """
            SUB_ZZ_Z
            Вычитание целых чисел
        """
        sign = "- " if self.sign else ""
        return sign + "".join(list(map(str, self.values)))
        def subtraction_integers(self, other):
        # Проверка на случай, если self равно нулю
        if self.values == [0] and other.values != [0]:  
            result = other.copy()
            result.sign = not other.sign  # Меняем знак результата
            return result
        # Если оба числа имеют одинаковый знак
        if self.check_sign() == other.check_sign():
        # Оба положительные
            if self.check_sign() == 2:
                if self.cmp_of_natural_number(other) == 1:
                    result = other.__sub__(self)  # Вычитаем большее из меньшего
                    result = Integers(result.n, result.values, True)  # Отрицательный результат
                elif self.cmp_of_natural_number(other) == 2:
                    result = self.__sub__(other)  # Вычитаем меньшее из большего
                    result = Integers(result.n, result.values, False)  # Положительный результат
                else:
                # Если числа равны, результат нулевой с положительным знаком
                    return Integers(1, [0], False)
        # Оба отрицательные
            else:
                if self.cmp_of_natural_number(other) == 1:
                    result = other.__sub__(self)
                    result = Integers(result.n, result.values, False)  # Положительный результат
                elif self.cmp_of_natural_number(other) == 2:
                    result = self.__sub__(other)
                    result = Integers(result.n, result.values, True)  # Отрицательный результат
                else:
                # Если числа равны, результат нулевой с положительным знаком
                    return Integers(1, [0], False)

    # Числа имеют разные знаки
        else:
            result = self.__add__(other.abs_integer())  # Складываем модули чисел
            result = Integers(result.n, result.values, self.sign)  # Сохраняем знак `self`

        return result


class Rational:
    """
    Класс, представляющий рациональное число.

    Рациональное число - это число, которое может быть представлено в виде дроби,
    где числитель - целый, знаменатель - натуральный

    Атрибуты:
      numerator: Объект класса Integers, представляющий числитель дроби.
      denominator: Объект класса Natural, представляющий знаменатель дроби.
    """
    def __init__(self, array_rational: list[Integers, Natural]):
        self.numerator = array_rational[0]  # числитель дроби
        self.denominator = array_rational[1]  # знаменатель дроби

    def __str__(self):
        return self.numerator.__str__() + "/" + self.denominator.__str__()


class Polynomial:
    """
    Класс, представляющий многочлен.

    В этом классе степень многочлена и его коэффициенты представлены
    объектами классов Natural и Rational соответственно.

    Атрибуты:
      degree: Объект класса Natural, представляющий степень многочлена.
      coefficients: Список объектов класса Rational, представляющий
             коэффициенты многочлена.
    """
    def __init__(self, array_polynomial: list[Natural, list[Rational]]):
        self.degree = array_polynomial[0]  # степень многочлена
        self.coefficients = array_polynomial[1]  # коэффиценты многочлена

    def degree_polynomial(self):
        """
            DEG_P_N
        Функция возвращает степень многочлена
        """
        return self.degree  # возвращает степень многочлена

    def __str__(self):
        result = ''
        for i in range(len(self.coefficients) - 1, - 1, -1):
            if self.coefficients[i].numerator.values != [0]:
                result += '+ ' if self.coefficients[i].numerator.sign is False else ''
                result += self.coefficients[i].__str__()
                if i != 0:
                    result += 'x^' + str(i)
                result += ' '
        if result[0] == '+':
            result = result[1:]
        return result


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
    return create_polynomial(coefficients, degrees, max_degree)


def create_polynomial(coefficients, degrees, max_degree):
    new_degrees = []
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



if __name__ == "__main__":
    a = int(input("Введите номер функции: "))
    Launch(a).start_function()

