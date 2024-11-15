from natural import Natural


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
        if sign == True and all([i == 0 for i in values]):
            raise ValueError("Нуль не может быть быть отрицательным!")
        super().__init__(n, values)
        self.sign = sign  # знак числа, если True, то минус

    def copy(self):
        # Создает и возвращает новый объект Integers, копируя значения текущего объекта
        return Integers(self.n, self.values.copy(), self.sign)

    def check_sign(self):
        """
        Выполнила Конасова Яна гр.3384
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
            Выполнила Котельникова Елизавета гр. 3384
            ABS_Z_N
            Функция берет модуль числа и возвращает его
        """
        if self.sign is True:  # проверяем знак
            self.sign = False  # если знак числа минус, то меняем знак на положительный
        return self  # выводим получившиеся число

    def invert_sign(self):
        """"
            Выполнила Полещук Виолетта гр. 3384
            MUL_ZM_Z
            Умножение целого на (-1)
        """
        number = self.copy()
        # Инвертирует знак текущего объекта, если он не равен 0 (если был False, станет True, и наоборот)
        if number.values != [0]:
            number.sign = (number.sign == False)
        # Возвращает текущий объект с инвертированным знаком
        return number

    def trans_in_natural(self):
        """
        Выполнил Козьмин Никита гр. 3384
        TRANS_Z_N
        Преобразование целого неотрицательного в натуральное
        """
        if self.sign == True:
            raise ValueError("Число не может быть отрицательное!")
        return Natural(self.n, self.values.copy())

    def trans_in_rational(self):
        from rational import Rational
        """
        Выполнил Козьмин Никита гр. 3384
        TRANS_Z_Q
        Преобразование целого в дробное
        """
        return Rational([self.copy(), Natural(1, [1])])

    def __add__(self, other):
        """"
            Выполнила Полещук Виолетта гр. 3384
            ADD_ZZ_Z
            Сложение целых чисел
        """
        integer_first = self.copy()
        integer_second = other.copy()
        # Проверяет, совпадают ли знаки обоих объектов
        if integer_first.sign == integer_second.sign:
            # Если знаки совпадают, выполняет сложение и возвращает новый объект с тем же знаком
            result = Natural.__add__(integer_first, integer_second)
            return Integers(result.n, result.values, integer_first.sign)
        # Если знаки не совпадают, сравнивает абсолютные значения чисел
        elif integer_first.cmp_of_natural_number(integer_second) == 2:
            # Если текущий объект больше по абсолютной величине, выполняет вычитание
            result = Natural.__sub__(integer_first, integer_second)
            # Определяет знак результата (оставляет знак текущего объекта, если результат не равен нулю)
            sign = integer_first.sign if result.values != [0] else False
            return Integers(result.n, result.values, sign)
        else:
            # Если текущий объект меньше по абсолютной величине, выполняет вычитание
            result = Natural.__sub__(integer_second, integer_first)
            # Определяет знак результата (оставляет знак другого объекта, если результат не равен нулю)
            sign = integer_second.sign if result.values != [0] else False
            return Integers(result.n, result.values, sign)

    def subtraction_integers(self, other):
        """"
            Выполнила Конасова Яна гр. 3384
            SUB_ZZ_Z
            Вычитание целых чисел
        """
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
            first_number, second_number = self.copy(), other.copy()
            result = (first_number.abs_integer()).__add__(second_number.abs_integer())
            result = Integers(result.n, result.values, self.sign)
        return result

    def __mul__(self, other):
        """"
        Выполнил Пак Кирилл гр. 3384
        MUL_ZZ_Z
        Функция для умножения целых чисел.
        """
        if (self.values[0] == 0 and self.n == 1) or (other.values[0] == 0 and other.n == 1):
            return Integers(1, [0], False)
        first_number = self.copy().abs_integer()  # создаем копии чисел, но без знака
        second_number = other.copy().abs_integer()
        first_sign = self.sign  # сохраняем знаки исходных чисел
        second_sign = other.sign
        if first_sign == second_sign:  # находим знак произведения 2 чисел
            new_number_sign = False
        else:
            new_number_sign = True

        first_number = first_number.trans_in_natural()
        second_number = second_number.trans_in_natural()
        res = first_number.__mul__(second_number)  # умножаем используя функцию умножения натуральных
        res = res.trans_in_integer(new_number_sign)  # превращаем число в целое и устанавливаем знак
        return res

    def div_integer(self, other):
        """
        Выполнил Пак Кирилл гр. 3384
        DIV_ZZ_Z
        Функция для нахождения частного от деления на ненулевое число
        """
        if not (super().number_is_not_zero()):  # Проверяем является ли делимое нулем
            return Integers(1, [0], False)
        else:
            dividend = self.copy().abs_integer()  # Создаем копии делимого и делителя
            divisor = other.copy().abs_integer()

            if self.sign == other.sign:  # Находим знак частного
                res_sign = False
            else:
                res_sign = True

            dividend = dividend.trans_in_natural()
            divisor = divisor.trans_in_natural()

            res = dividend.div_natural(divisor)  # Находим частное от деления

            if not (res.number_is_not_zero()):  # Проверяем, является ли частное нулем
                return Integers(1, [0], False)

            if self.sign == True and dividend.__sub__(
                    divisor.__mul__(res)).number_is_not_zero():  # Проверяем может ли быть остаток отрицательным.
                res = res.__add__(Integers(1, [1], False))
            res = res.trans_in_integer(res_sign)  # Добавляем знак

            return res

    def mod_integer(self, other):
        """
        Выполнил Пак Кирилл гр. 3384
        MOD_ZZ_Z
        Остаток от деления целого на целое(делитель отличен от нуля)
        """
        dividend = self.copy()  # делаем копии делимого и делителя
        divisor = other.copy()

        quotlent = dividend.div_integer(divisor)  # находим частное

        mod = dividend.subtraction_integers(divisor.__mul__(quotlent))  # находим остаток от деления

        return mod

    def __str__(self):
        sign = "- " if self.sign else ""
        return sign + "".join(list(map(str, self.values)))