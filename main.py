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

    def number_is_not_zero(self):
        """
        NZER_N_B
        Функция которое проверяет является ли число не нулевым.
        Если число равно 0 возвращает False, иначе True.
        """
        return not (self.n == 1 and self.values[0] == 0)


    def __mul__(self, number):
        """
            MUL_ND_N
            Умножение натурального числа на цифру
        """
        answer = [0] * (self.n + 1)  # Создаем список нулей длиной n + 1 для хранения результата
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

    def increment(self):
        """
            ADD_1N_N
            Добавление 1 к натуральному числу
        """
        number = self.copy()
        # Начинаем с последней цифры, увеличивая её на 1
        shift = (number.values[number.n - 1] + 1) // 10  # Определяем, потребуется ли перенос
        number.values[number.n - 1] = (number.values[number.n - 1] + 1) % 10  # Обновляем последнюю цифру

        # Если перенос остался после изменения последней цифры, идем по остальным разрядам
        if shift != 0:
            for index in range(number.n - 2, -1, -1):  # Проходим от предпоследнего элемента к первому
                num = number.values[index]  # Берем значение текущего разряда
                number.values[index] = (num + shift) % 10  # Добавляем перенос и записываем результат в текущий разряд
                shift = (num + shift) // 10  # Пересчитываем перенос для следующего разряда

                # Если перенос больше не нужен, выходим из цикла
                if shift == 0:
                    break

        # Если перенос остался после обработки всех разрядов, добавляем его в старший разряд
        if shift == 1:
            number.values.insert(0, 1)  # Вставляем 1 в начало массива, чтобы отразить перенос
            number.n += 1  # Увеличиваем длину числа, так как добавился новый разряд
        return number

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


    def multiply_by_ten(self, k):
        """
        MUL_Nk_N
        Функция умножения натурального числа на 10^k
        """
        if not(self.number_is_not_zero()):
            return self
        res = self.copy() #создаем копию числа
        res.values = res.values + [0] * k #добавляем в конец числа k 0
        res.n += k #увеличиваем длину на k
        return res


    def multiply(self,other):
        """
        MUL_NN_N
        Функция для умножения 2 натуральных чисел.
        """
        cmp = self.cmp_of_natural_number(other)  # сравниваем 2 числа, чтобы понять какое число больше.

        if cmp == 2 or cmp == 0: # Копируем больший элемент в larger_number, а меньший в lower_number
            larger_number = self.copy()
            lower_number= other.copy()
        else:
            lower_number = self.copy()
            larger_number = other.copy()

        lower_number.values.reverse()
        res = Natural(1,[0])
        k = 0
        for i in range(lower_number.n): # Проходим по разрядам меньшего элемента и умножаем их на большее число
            tmp = larger_number.__mul__(lower_number.values[i])
            tmp = tmp.multiply_by_ten(k)
            res = res.__add__(tmp) # Суммируем произведение большего числа на цифру меньшего, умноженное на 10^k
            k += 1
        return res


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

    def copy(self):
        # Создает и возвращает новый объект Integers, копируя значения текущего объекта
        return Integers(self.n, self.values.copy(), self.sign)

    def check_sign(self):
        """
        POZ_Z_D
        Определение положительности числа. (0-число равно 0, 1 - отрицательное, 2 - положительное)
        """
        if (self.n == 1 and self.values[0] == 0):  # Проверяем, является ли число нулем
            return 0
        else:
            if not (self.sign):  # Проверем отрицательное (sign = true) число или нет
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

    def invert_sign(self):
        """"
            MUL_ZM_Z
            Умножение целого на (-1)
        """
        number = self.copy()
        # Инвертирует знак текущего объекта, если он не равен 0 (если был False, станет True, и наоборот)
        if number.values != [0]:
            number.sign = (number.sign == False)
        # Возвращает текущий объект с инвертированным знаком
        return number

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

    def copy(self):
        # Создает и возвращает новый объект Rational, копируя значения текущего объекта
        return Rational([self.numerator.copy(), self.denominator.copy()])

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

    def copy(self):
        # Создает и возвращает новый объект Polynomial, копируя значения текущего объекта
        return Polynomial([self.degree.copy(), self.coefficients.copy()])

    def degree_polynomial(self):
        """
            DEG_P_N
        Функция возвращает степень многочлена
        """
        return self.degree  # возвращает степень многочлена

    def multiply_by_monomial(self, k):
        """
        MUL_Pxk_P
        Умножение многочлена на x^k, k-натуральное или 0
        """
        # Создаем копию текущего полинома, чтобы не изменять оригинал.
        polynomial = self.copy()

        # Устанавливаем степень полинома равной k.
        polynomial.degree = k

        # Создаем объект Natural, представляющий число 1.
        one = Natural(1, [1])

        # Создаем копию k, чтобы не изменять оригинальное значение.
        k = k.copy()

        # Пока k не равно 0, добавляем нулевые коэффициенты в начало списка коэффициентов полинома.
        while k.cmp_of_natural_number(Natural(1, [0])) != 0:
            # Добавляем нулевой коэффициент в начало списка коэффициентов.
            polynomial.coefficients.insert(0, Rational([Integers(1, [0], False), one]))

            # Уменьшаем k на 1.
            k = k - one

        # Возвращаем полином, умноженный на одночлен.
        return polynomial

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
            print(natural.multiply(natural_second))


if __name__ == "__main__":
    a = int(input("Введите номер функции: "))
    Launch(a).start_function()
