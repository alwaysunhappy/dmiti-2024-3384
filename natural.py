from input_create import create_natural


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
        Выполнил Кирилл Пак гр. 3384
        NZER_N_B
        Функция которое проверяет является ли число не нулевым.
        Если число равно 0 возвращает False, иначе True.
        """
        return not (self.n == 1 and self.values[0] == 0)

    def multiplication_by_digit(self, number):
        """
            Выполнил Баяндин Дмитрий гр.3384
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
            Выполнила Котельникова Лиза гр.3384
            COM_NN_D
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
            Выполнила Полещук Виолетта гр. 3384
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
            Выполнил Баяндин Дмитрий гр.3384
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
                #  переносим десяток на следующий разряд, если это нужно
                if answer[-i] > 9:
                    answer[-i] -= 10
                    shift = 1
            elif larger_number.n >= i:  # когда у второго числа уже нечего складывать
                answer[-i] = larger_number.values[-i] + shift
                shift = 0
                #  переносим десяток на следующий разряд, если это нужно
                if answer[-i] > 9:
                    answer[-i] -= 10
                    shift = 1
            else:
                answer[-i] = shift  # обрабатываем случай, если перенос случился на первом разрде (1 + 99 = 100)
                # <- здесь запишем единицу

        natural = create_natural(answer)
        natural.del_leader_zero()
        return natural

    def __sub__(self, other):
        """
            Выполнил Баяндин Дмитрий гр.3384
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

            # будет занимать, пока это необхдимо (как при вычитании столбик "руками")
            while larger_number.values[j] < 0:
                # текущему разряду прибавляем десяток, а у следущего отнимаем (занимаем)
                larger_number.values[j] += 10
                larger_number.values[j - 1] -= 1
                j -= 1

        natural = create_natural(larger_number.values)
        natural.del_leader_zero()
        return natural

    def multiply_by_ten(self, k):
        """
        Выполнил Пак Кририлл гр.3384
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

    def __mul__(self, other):
        """
        Выполнил Пак Кирилл гр. 3384
        MUL_NN_N
        Функция для умножения 2 натуральных чисел.
        """
        if (self.number_is_not_zero() == False) or (other.number_is_not_zero() == False):
            return Natural(1, [0])

        cmp = self.cmp_of_natural_number(other)  # сравниваем 2 числа, чтобы понять какое число больше.

        if cmp == 2 or cmp == 0:  # Копируем больший элемент в larger_number, а меньший в lower_number
            larger_number = self.copy()
            lower_number = other.copy()
        else:
            lower_number = self.copy()
            larger_number = other.copy()

        res = Natural(1, [0])
        k = create_natural([0])
        for i in range(-1, -lower_number.n - 1,
                       -1):  # Проходим по разрядам меньшего элемента и умножаем их на большее число(эти действия аналогичные умножению в столбик)
            tmp = larger_number.multiplication_by_digit(lower_number.values[i])
            tmp = tmp.multiply_by_ten(k)
            res = res.__add__(tmp)  # Суммируем произведение большего числа на цифру меньшего, умноженное на 10^k
            k += create_natural([1])
        return res

    def trans_in_integer(self, sign: bool = False):
        from integers import Integers
        """
        Выполнил Козьмин Никита гр. 3384
        TRANS_N_Z
        Преобразование натурального в целое
        """
        return Integers(self.n, self.values.copy(), sign)

    def subtract_scaled_natural(self, other, number):
        """
        Выполнил Траксель Виталий гр. 3384
        SUB_NDN_N
        Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом
        """
        mul = other.multiplication_by_digit(number)  # Умножение второго натурального на цифру
        if self.cmp_of_natural_number(mul) != 1:  # Проверка на то, что при вычетании будет неотрицательный результат
            return self.__sub__(mul)  # вычитание

    def first_digit__of_scaled_division(self, other):
        """
        Выполнил Траксель Виталий гр.3384
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
        Выполнил Траксель Виталий гр.3384
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
        Выполнил Траксель Виталий гр.3384
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

    def gcf_natural(self, other):
        """
        Выполнил Хальзев Александр гр. 3384
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
        Выполнил Хальзев Александр гр.3384
        LCM_NN_N
        НОК натуральных чисел.
        """
        return self.__mul__(other).div_natural(self.gcf_natural(other))

    def __str__(self):
        return "".join(list(map(str, self.values)))
