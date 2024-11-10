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

    def multiplication_by_digit(self, number):
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
            if smaller_number.n >= i:  # если у меньшего числа еще есть что складывать
                answer[-i] = larger_number.values[-i] + smaller_number.values[-i] + shift
                shift = 0
                if answer[-i] > 9:
                    answer[-i] -= 10
                    shift = 1
            elif larger_number.n >= i:  # когда у второго числа уже нечего складывать
                answer[-i] = larger_number.values[-i] + shift
                shift = 0
                if answer[-i] > 9:
                    answer[-i] -= 10
                    shift = 1
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

        for i in range(1, smaller_number.n + 1):  # Начинаем перебор разрядов с последнего
            larger_number.values[-i] = larger_number.values[-i] - smaller_number.values[-i]

            j = -i

            while larger_number.values[j] < 0:
                larger_number.values[j] += 10
                larger_number.values[j - 1] -= 1
                j -= 1


        natural = create_natural(larger_number.values)
        natural.del_leader_zero()
        return natural

    def multiply_by_ten(self, k):
        """
        MUL_Nk_N
        Функция умножения натурального числа на 10^k
        """
        if not (self.number_is_not_zero()):
            return self
        natural = self.copy()  # создаем копию числа
        degree = k.copy()
        while degree.values != [0]:
            natural.values.append(0)
            natural.n += 1
            degree = degree.__sub__(create_natural([1]))
        return natural

    def __mul__(self,other):
        """
        MUL_NN_N
        Функция для умножения 2 натуральных чисел.
        """
        if (self.number_is_not_zero() == False ) or (other.number_is_not_zero() == False ):
            return Natural(1, [0])

        cmp = self.cmp_of_natural_number(other)  # сравниваем 2 числа, чтобы понять какое число больше.

        if cmp == 2 or cmp == 0: # Копируем больший элемент в larger_number, а меньший в lower_number
            larger_number = self.copy()
            lower_number= other.copy()
        else:
            lower_number = self.copy()
            larger_number = other.copy()

        res = Natural(1,[0])
        k = create_natural([0])
        for i in range(-1, -lower_number.n - 1, -1): # Проходим по разрядам меньшего элемента и умножаем их на большее число(эти действия аналогичные умножению в столбик)
            tmp = larger_number.multiplication_by_digit(lower_number.values[i])
            tmp = tmp.multiply_by_ten(k)
            res = res.__add__(tmp) # Суммируем произведение большего числа на цифру меньшего, умноженное на 10^k
            k += create_natural([1])
        return res

    def trans_in_integer(self, sign: bool = False):
        """
        TRANS_N_Z
        Преобразование натурального в целое
        """
        return Integers(self.n, self.values.copy(), sign)
      
    def subtract_scaled_natural(self, other, number):
        """
        SUB_NDN_N
        Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом
        """
        mul = other.multiplication_by_digit(number) # Умножение второго натурального на цифру
        if self.cmp_of_natural_number(mul) != 1: # Проверка на то, что при вычетании будет неотрицательный результат
            return self.__sub__(mul) # вычитание

    def first_digit__of_scaled_division(self, other):
        """
        Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k,
        где k - номер позиции этой цифры (номер считается с нуля)
        DIV_NN_Dk
        """
        if other.number_is_not_zero() is False:
            raise ZeroDivisionError
        larger_number, smaller_number = self.copy(), other.copy()
        #  уменьшаем количество разрядов большего числа до количества разрядов второго
        larger_number.values = larger_number.values[:smaller_number.n]
        larger_number.n = len(larger_number.values)
        # если меньшее число оказалось больше после уменьшение кол-ва разрядов большего, добавляем еще один разряд
        if larger_number.cmp_of_natural_number(smaller_number) == 1:
            larger_number.values = self.values[:smaller_number.n + 1]
        larger_number.n = len(larger_number.values)  # обновили длину большего
        # находим k
        k = create_natural([int(i) for i in str(self.n - larger_number.n)])
        answer = create_natural([0])
        # находим первую цифру при делении большего на меньшее
        while larger_number.cmp_of_natural_number(smaller_number) != 1:
            larger_number = larger_number.__sub__(smaller_number)
            answer += create_natural([1])
        #  умножаем найденную первую цифру на 10^k
        return answer.multiply_by_ten(k)

    def div_natural(self, other):
        """
        Неполное частное от деления первого натурального числа на второе с остатком (делитель отличен от нуля)
        DIV_NN_N
        """
        larger_number, smaller_number = self.copy(), other.copy()
        if other.number_is_not_zero() is False:
            raise ZeroDivisionError
        answer = create_natural([0])
        #  пока larger_number >= smaller_number
        while larger_number.cmp_of_natural_number(smaller_number) != 1:
            # получаем первую цифру частного, домноженную на 10^k
            first_digit_with_zeros = larger_number.first_digit__of_scaled_division(smaller_number)
            #  вычитаем из делимого полученного значение, умноженное на делитель
            larger_number = larger_number.__sub__(first_digit_with_zeros.__mul__(smaller_number))
            #  увеличиваем ответ
            answer = answer.__add__(first_digit_with_zeros)
        return answer

    def mod_natural(self, other):
        """
        Остаток от деления первого натурального числа на второе натуральное (делитель отличен от нуля)
        MOD_NN_N
        """
        larger_number, smaller_number = self.copy(), other.copy()
        if other.number_is_not_zero() is False:
            raise ZeroDivisionError
        # остаток можно выразить из формулы larger_number = mod(larger_number, smaller_number) + div(larger_number,
        # smaller_number) * smaller_number
        result_div = larger_number.div_natural(smaller_number)  # получили неполное частное
        result_mul = result_div.__mul__(smaller_number)  # домножили на делитель
        return larger_number.__sub__(result_mul)  # вернули остаток от деления
    
    def __str__(self):
        return "".join(list(map(str, self.values)))
    
    def gcf_natural(self, other):
        """
        GCF_NN_N
        Вычисление наибольшего общего делителя двух натуральных чисел.
        """
        a, b = self, other

        # Пока одно из чисел не станет нулем
        while b.number_is_not_zero():
            remainder = a.mod_natural(b)
            if not remainder.number_is_not_zero():  # если остаток равен нулю
                return b  # возвращаем делитель, так как a делится на b
            a, b = b, remainder

        return a

    def lmc_natural(self, other):
        """
        LCM_NN_N
        НОК натуральных чисел.
        """
        return self.__mul__(other).div_natural(self.gcf_natural(other))

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

    def trans_in_natural(self):
        """
        TRANS_Z_N
        Преобразование целого неотрицательного в натуральное
        """
        if self.sign == True:
            raise ValueError("Число не может быть отрицательное!")
        return Natural(self.n, self.values.copy())
    
    def trans_in_rational(self):
        """
        TRANS_Q_Z
        Преобразование целого в дробное
        """
        return Rational([self.copy(), Natural(1, [1])])

    def __add__(self, other):
        """"
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
        
    def __str__(self):
        sign = "- " if self.sign else ""
        return sign + "".join(list(map(str, self.values)))

    def subtraction_integers(self, other):
        """"
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
        res = first_number.__mul__(second_number)# умножаем используя функцию умножения натуральных
        res = res.trans_in_integer(new_number_sign)  # превращаем число в целое и устанавливаем знак
        return res

    def div_integer(self, other):
        """
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

            if self.sign == True and dividend.__sub__(divisor.__mul__(res)).number_is_not_zero(): #Проверяем может ли быть остаток отрицательным.
                res = res.__add__(Integers(1, [1], False))
            res = res.trans_in_integer(res_sign)  # Добавляем знак

            return res

    def mod_integer(self, other):
        dividend = self.copy()  #делаем копии делимого и делителя
        divisor = other.copy()

        quotlent = dividend.div_integer(divisor) #находим частное

        mod = dividend.subtraction_integers(divisor.__mul__(quotlent)) # находим остаток от деления

        return mod


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

    def trans_in_integer(self):
        if self.denominator.values != [1]:
            raise ValueError("Знаменатель должен быть единицой!")
        return self.numerator.copy()
    
    def __str__(self):
        return self.numerator.__str__() + "/" + self.denominator.__str__()
        
    def int_check(self):
        """
        Проверка сокращенного дробного на целое, если рациональное число является целым, то True, иначе False
        """
        num = self.numerator
        den = self.denominator
        num = num.abs_integer().trans_in_natural()
        comp = num.cmp_of_natural_number(den)
    
        if comp == 0:
            return True
    
        if comp == 1:
            return False
    
        if comp == 2:
            while num.cmp_of_natural_number(den) == 2:
                den = den.__add__(den)
            if num.cmp_of_natural_number(den) == 0:
                return True
            else:
                return False
     
    def sub_rat(self, other):
        """
            SUB_QQ_Q
            Вычитание дробей.
        """
        dom1 = self.denominator
        dom2 = other.denominator
        domin = dom1.lmc_natural(dom2)
        coef1 = domin.div_natural(dom1)
        coef2 = domin.div_natural(dom2)
        new_num1 = self.numerator.__mul__(Integers(len(coef1.values), coef1.values, False))
        new_num2 = other.numerator.__mul__(Integers(len(coef2.values), coef2.values, False))
        fin_num = new_num1.subtraction_integers(new_num2)
        if fin_num.values==[0]:
            return Rational([fin_num, Natural(1, [1])])
        return Rational([fin_num, domin])

    def __mul__(self, other):
        """"
        MUL_QQ_Q
        Функция созданная для умножения дробей.
        """
        f_number = self.copy() # Создаем копии чисел
        s_number = other.copy()

        new_numerator = f_number.numerator.__mul__(s_number.numerator) # Считаем числитель
        new_denominator = f_number.denominator.__mul__(s_number.denominator) # Считаем знаменатель

        res = Rational([new_numerator , new_denominator]) # Создаем дробь из числителя и знаменателя

        return res

    def fraction_reduction(self):
        """
            RED_Q_Q
            Сокращение дроби
        """
        fraction = self.copy()  # сделали копию
        remembered_sign = self.numerator.sign  # запомнили знак
        if remembered_sign is True:
            fraction.numerator = fraction.numerator.abs_integer()  # взяли модуль от числителя, чтобы использовать НОД
        gcf = fraction.denominator.gcf_natural(fraction.numerator)  # нашли НОД числителя и знаменателя
        if remembered_sign is True:
            fraction.numerator.sign = True  # вернули знак числителю
        if gcf != 1:  # Если НОД больше одного, делим числитель и знаменатель на их НОД
            fraction.numerator = fraction.numerator.div_integer(gcf.trans_in_integer())
            fraction.denominator = create_integer(fraction.denominator.values, False).div_integer(gcf.trans_in_integer())
        fraction.numerator.n = len(self.numerator.values)  # записали новую длину
        fraction.denominator.n = len(self.denominator.values)
        return fraction

    def division_of_fractions(self, other):
        """
            DIV_QQ_Q
            Деление дробей (делитель отличен от нуля)
        """
        first_fraction, second_fraction = self.copy(), other.copy()
        remembered_sign = first_fraction.numerator.sign != second_fraction.numerator.sign
        #  умножили числитель первой дроби на знаменатель второй дроби
        first_fraction.numerator = first_fraction.numerator.__mul__(second_fraction.denominator.trans_in_integer())
        result = second_fraction.numerator.__mul__(first_fraction.denominator.trans_in_integer())
        first_fraction.denominator = Natural(result.n, result.values)
        first_fraction.numerator.sign = remembered_sign
        return first_fraction
    
    def __add__(self, other):
        """
            ADD_QQ_Q
            Сложение дробей
        """
        # Находим наименьшее общее кратное (НОК) знаменателей двух дробей.
        lcm =  self.denominator.lmc_natural(other.denominator)
        
        # Вычисляем множители, на которые нужно умножить числители,
        # чтобы привести дроби к общему знаменателю.
        
        multiplier_first = lcm.div_natural(self.denominator).trans_in_integer()

        multiplier_second = lcm.div_natural(other.denominator).trans_in_integer() 

        # Складываем числители, умноженные на соответствующие множители.
        numerator1 = self.numerator.__mul__(multiplier_first) 
        numerator2 = other.numerator.__mul__(multiplier_second)
        result_numerator = numerator1.__add__(numerator2)
        # Создаем результирующую дробь с полученным числителем и общим знаменателем.
        result = Rational([result_numerator, lcm])
        return result


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
        
    def add_pol(self, other):
        """
            Add_PP_P.
            Сложение многочленов.
        """
        arr = []
        diff = self.degree.cmp_of_natural_number(other.degree)
        if diff == 2:
            mini = int(''.join(map(str, other.degree.values)))
        else:
            mini = int(''.join(map(str, self.degree.values)))
        for i in range(mini + 1):
            n = self.coefficients[i].__add__(other.coefficients[i])
            arr.append(n)
        if diff == 2:
            for i in range(mini + 1, int(''.join(map(str, self.degree.values))) + 1):
                arr.append(self.coefficients[i])
            return Polynomial([self.degree, arr])
        if diff == 1:
            for i in range(mini + 1, int(''.join(map(str, other.degree.values))) + 1):
                arr.append(other.coefficients[i])
            return Polynomial([other.degree, arr])
        while arr[-1].numerator.values == [0]:
            arr = arr[:-1]
        mini = Natural(len([int(x) for x in str(len(arr) - 1)]), [int(x) for x in str(len(arr) - 1)])
        return Polynomial([mini, arr])

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

        polynomial.degree = create_natural([int(i) for i in str(len(polynomial.coefficients) - 1)])
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
     
    def pol_derivative(self):
        '''
            DER_P_P
            Возвращает производную многочлена.
        '''
        coeffs = self.coefficients[1:]
        new_coeffs = []
        deg = 1
        for coef in coeffs:
            value = coef.numerator.abs_integer().trans_in_natural().multiplication_by_digit(deg).values
            Int_coef = Integers(len(value), value, coef.numerator.sign)
            coef = Rational([Int_coef, coef.denominator])
            new_coeffs.append(coef)
            deg += 1
        return Polynomial([self.degree.multiplication_by_digit(1), new_coeffs])
    
    def leading_coefficient(self):
        """
        LED_P_Q
        Возвращает старший коэффициент многочлена.
        """
        # Ищем первый ненулевой коэффициент, начиная с конца списка
        for coefficient in reversed(self.coefficients):
            if coefficient.numerator.values != [0]:  # проверяем, что коэффициент не равен нулю
                return coefficient
        return None  # возвращаем None, если все коэффициенты нулевые
    
    def multiply_by_scalar(self, scalar):
        """
        MUL_PQ_P
        Умножение многочлена на рациональное число
        """
        polynomial = self.copy()
        polynomial.coefficients = [number.__mul__(scalar) for number in polynomial.coefficients]
        return polynomial
    
    def subtract_polynomial(self, other):
        """
        SUB_PP_P
        Вычитание многочленов.
        """
        f_pol = self.copy()
        s_pol = other.copy()
        arr = []  # Список для хранения новых коэффициентов
        # Определяем минимальную степень (по индексу), чтобы пройти по всем коэффициентам, которые присутствуют в обоих многочленах
        min_degree = min(len(f_pol.coefficients), len(s_pol.coefficients)) - 1
        # Вычитаем коэффициенты до минимальной степени (наименьшей длины списка коэффициентов)
        for i in range(min_degree + 1):
            arr.append(f_pol.coefficients[i].sub_rat(s_pol.coefficients[i]))
        # Если первый многочлен имеет большую степень, добавляем оставшиеся коэффициенты
        if len(f_pol.coefficients) > len(s_pol.coefficients):
            arr.extend(f_pol.coefficients[min_degree + 1:])
        # Если второй многочлен имеет большую степень, добавляем оставшиеся коэффициенты со знаком минус
        elif len(s_pol.coefficients) > len(f_pol.coefficients):
            for i in range(min_degree + 1, len(s_pol.coefficients)):
                num = s_pol.coefficients[i].numerator.values
                denum = s_pol.coefficients[i].denominator
                # Создаем коэффициент с отрицательным знаком
                negative_coef = Rational([Integers(len(num), num, True), denum])
                arr.append(negative_coef)
        # Удаляем ведущие нулевые коэффициенты, если они есть
        while arr and arr[-1].numerator.values == [0]:
            arr.pop()
        # Если после всех операций все коэффициенты оказались нулевыми, то это нулевой многочлен, степень которого равна 0
        if arr:
            # Определяем новую степень многочлена по количеству ненулевых коэффициентов
            new_degree = Natural(len(str(len(arr) - 1)), [int(x) for x in str(len(arr) - 1)])
        else:
            new_degree = Natural(1, [0])  # Нулевой многочлен степени 0
        return Polynomial([new_degree, arr])
    
    def factor_polynomial(self):
        """
        FAC_P_Q
        Вынесение из многочлена НОК знаменателей и НОД числителей
        """
        polynomial = self.copy()
        # Получаем списки числителей и знаменателей для каждого коэффициента
        numerators = [coeff.numerator for coeff in polynomial.coefficients]
        denominators = [coeff.denominator for coeff in polynomial.coefficients]
        # Находим НОД числителей и НОК знаменателей
        gcf_num = numerators[0]
        lcm_den = denominators[0]
        # Вычисляем НОД
        for num in numerators[1:]:
            gcf_num = gcf_num.gcf_natural(num)
        # Вычисляем НОК
        for denom in denominators[1:]:
            lcm_den = lcm_den.lmc_natural(denom)
        gcf_num_int = Integers(gcf_num.n, gcf_num.values, sign=False)
        # Создаем общий множитель (НОД числителей и НОК знаменателей)
        common_factor = Rational([gcf_num_int, lcm_den])
        for i in range(len(polynomial.coefficients)):
            polynomial.coefficients[i] = polynomial.coefficients[i].division_of_fractions(common_factor)
        return polynomial
    
    def polynomial_remainder(self, other):
        """
        MOD_PP_P
        Вычисляет остаток от деления многочлена на многочлен при делении с остатком.
        """
        f_pol = self.copy()
        s_pol = other.copy()
        if f_pol.degree.cmp_of_natural_number(s_pol.degree) == 1:
            raise ValueError("Степень делимого меньше степени делителя. Невозможно выполнить деление.")
        # Выполнение деления многочленов для получения частного
        quotient = f_pol.div_polynom(s_pol)
        # Умножаем частное на делитель, чтобы получить произведение
        product = quotient.__mul__(s_pol)
        # Вычитаем произведение из делимого многочлена, чтобы получить остаток
        remainder = f_pol.subtract_polynomial(product)
        return remainder

    def __mul__(self, other):
        #создаем полином для записи ответа
        answer = Polynomial([create_natural([0]), [create_rational(create_integer([0], False), create_natural([1]))]])

        #сделали копии полиномов
        first_pol = self.copy()
        second_pol = other.copy()

        #  перебираем по количеству слагаемых во втором многочлене
        for i in range(len(second_pol.coefficients)):
            # умножаем первый полином на x^i
            multiply_xi = first_pol.multiply_by_monomial(create_natural([int(j) for j in str(i)]))
            #умножаем первый полином на коэффициент соответсвующий слагаемому степени x^i и прибавляем его к ответу
            answer = answer.add_pol(multiply_xi.multiply_by_scalar(second_pol.coefficients[i]))

        return answer

    def div_polynom(self, other):
        # если степень второго полинома больше, чем степень первого, частное будет равно 0
        if self.degree.cmp_of_natural_number(other.degree) == 1:
            return Polynomial([create_natural([0]), [create_rational(create_integer([0], False), create_natural([1]))]])

        #сделали копии полиномов
        first_pol = self.copy()
        second_pol = other.copy()

        # создаем полином для записи ответа
        answer = Polynomial([create_natural([0]), [create_rational(create_integer([0], False), create_natural([1]))]])

        # будет делить, пока степень делимого больше или равна степени делителя, либо не равна 0
        while first_pol.degree.cmp_of_natural_number(second_pol.degree) != 1 and first_pol.degree.number_is_not_zero():
            # получаем коэффициент домножения делителя (отношение старших коэффициентов)
            ratio = first_pol.coefficients[-1].division_of_fractions(second_pol.coefficients[-1])
            # прибавляем к результату одночлен, с коэффициентом ratio и степенью равной разности степеней делимого и делителя
            answer = answer.add_pol((Polynomial([create_natural([0]), [ratio]])).multiply_by_monomial(first_pol.degree - second_pol.degree))
            # вычитаем из делимого полином, полученный умножением одночлена на делитель
            first_pol = first_pol.subtract_polynomial(second_pol.multiply_by_monomial(first_pol.degree - second_pol.degree).multiply_by_scalar(ratio))
        return answer


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
