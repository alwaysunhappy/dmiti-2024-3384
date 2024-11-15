from natural import Natural
from integers import Integers


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
        """
        Выполнил Козьмин Никита гр. 3384
        TRANS_Q_Z
        Преобразование сокращенного дробного в целое (если знаменатель равен 1)
        """
        if self.denominator.values != [1]:
            raise ValueError("Знаменатель должен быть единицой!")
        return self.numerator.copy()

    def int_check(self):
        """
        Выполнил Александр Хальзев гр. 3384
        INT_Q_B
        Проверка сокращенного дробного на целое, если рациональное число является целым, то True, иначе False
        """
        num = self.numerator
        den = self.denominator
        den1 = den
        # сравнение числителя со знаменателем
        num = num.abs_integer().trans_in_natural()
        comp = num.cmp_of_natural_number(den)
        # если числитель == знаменателю, то True
        if comp == 0:
            return True
        # если знаменатель больше сразу False
        if comp == 1:
            return False

        if comp == 2:
            # пока числитель больше знаменателя, умножаем знаменатель, пока тот не превысит или станет равным числителю
            while num.cmp_of_natural_number(den) == 2:
                den = den.__add__(den1)
            # если стал равен то True иначе False
            if num.cmp_of_natural_number(den) == 0:
                return True
            else:
                return False

    def sub_rat(self, other):
        """
            Выполнила Конасова Яна гр. 3384
            SUB_QQ_Q
            Вычитание дробей.
        """
        dom1 = self.denominator
        dom2 = other.denominator
        # нахождение общего делителя, используя НОК
        domin = dom1.lmc_natural(dom2)
        # нахождение коэффициетов умножения
        coef1 = domin.div_natural(dom1)
        coef2 = domin.div_natural(dom2)
        # умножение этих коэффициетнов на числители
        new_num1 = self.numerator.__mul__(Integers(len(coef1.values), coef1.values, False))
        new_num2 = other.numerator.__mul__(Integers(len(coef2.values), coef2.values, False))
        # вычитание приведенных числителей
        fin_num = new_num1.subtraction_integers(new_num2)
        # если в результате получился 0 в числителе, то знаменатель = 1
        if fin_num.values == [0]:
            return Rational([fin_num, Natural(1, [1])])
        return Rational([fin_num, domin])

    def __mul__(self, other):
        """"
            Выполнил Пак Кирилл гр. 3384
            MUL_QQ_Q
            Функция созданная для умножения дробей.
        """
        f_number = self.copy()  # Создаем копии чисел
        s_number = other.copy()

        new_numerator = f_number.numerator.__mul__(s_number.numerator)  # Считаем числитель
        new_denominator = f_number.denominator.__mul__(s_number.denominator)  # Считаем знаменатель

        res = Rational([new_numerator, new_denominator])  # Создаем дробь из числителя и знаменателя

        return res

    def fraction_reduction(self):
        """
            Выполнила Котельникова Елизавета гр. 3384
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
            fraction.denominator = fraction.denominator.div_natural(gcf)
        fraction.numerator.n = len(self.numerator.values)  # записали новую длину
        fraction.denominator.n = len(self.denominator.values)
        return fraction

    def division_of_fractions(self, other):
        """
            Выполнила Котельникова Елизавета гр. 3384
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
            Выполнила Полещук Виолетта гр. 3384
            ADD_QQ_Q
            Сложение дробей
        """
        # Находим наименьшее общее кратное (НОК) знаменателей двух дробей.
        lcm = self.denominator.lmc_natural(other.denominator)

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

    def __str__(self):
        other = self.fraction_reduction()
        return other.numerator.__str__() + "/" + other.denominator.__str__()