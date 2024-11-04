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

    def multiplication_by_digit(self, number):
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

    def __add__(self, other):
        """
            ADD_NN_N
            Складывает два натурльных числа и возвращает результат
        """
        if self.cmp_of_natural_number(other) == 1:  # если второе значение больше
            larger_number, smaller_number = other.copy(), self.copy()
        else:
            larger_number, smaller_number = self.copy(), other.copy()

        shift = 0  # перенос в следущий разряд
        answer = [0] * (larger_number.n + 1)  # массив длиной на один разряд больше большего числа
        for i in range(1, larger_number.n + 2):  # перебираем -1 индекс,-2 индекс и т.д.
            if smaller_number.n >= i:  # если у меньшего числа еще есть, что складывать
                total = larger_number.values[-i] + smaller_number.values[-i] + shift
                answer[-i] = total % 10  # получаем цифру которая запишется в этом разряде
                shift = total // 10  # считаем перенос на след разряд
            elif larger_number.n >= i:  # когда у второго числа уже нечего складывать
                total = larger_number.values[-i] + shift
                answer[-i] = total % 10
                shift = total // 10
            else:
                answer[-i] = shift  # обрабатываем случай, если перенос случился на первом разрде (9 + 99 = 18)
                # <- здесь запишем единицу

        natural = create_natural(answer)
        natural.del_leader_zero()
        return natural

    def __sub__(self, other):
        """
            SUB_NN_N
            Вычитание натуральных чисел
        """
        if self.cmp_of_natural_number(other) == 1:  # если второе значение больше
            larger_number, smaller_number = other.copy(), self.copy()
        else:
            larger_number, smaller_number = self.copy(), other.copy()
        carry = 0  # Переменная для учета переноса (если предыдущий разряд занял десятку)
        # Инициализируем массив для ответа, размер которого равен размеру большего числа
        answer = [0] * larger_number.n
        for i in range(1, larger_number.n + 1):  # Начинаем перебор разрядов с последнего
            if smaller_number.n >= i:  # Если у меньшего числа есть разряд, который можно вычесть
                total = larger_number.values[-i] - smaller_number.values[-i] - carry
                # Если большему числу не хватает для вычитания, добавляем 10 и устанавливаем перенос
                if total < 0:
                    total += 10
                    carry = 1
                else:
                    carry = 0
                answer[-i] = total
            # Если у большего числа есть разряд, но у меньшего нет
            elif larger_number.n >= i:
                if larger_number.values[-i] == 0 and carry:  # если мы занимали, но след. разряд 0, нужно снова занять
                    total = larger_number.values[-i] - carry + 10
                else:
                    total = larger_number.values[-i] - carry
                    carry = 0
                answer[-i] = total

        natural = create_natural(answer)
        natural.del_leader_zero()
        return natural
    
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

    def abs_integer(self):
        """
            ABS_Z_N
            Функция берет модуль числа и возвращает его
        """
        if self.sign is True:  # проверяем знак
            self.sign = False  # если знак числа минус, то меняем знак на положительный
        return self  # выводим получившиеся число

    def __str__(self):
        sign = "- " if self.sign else ""
        return sign + "".join(list(map(str, self.values)))


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

