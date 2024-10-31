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
