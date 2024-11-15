from natural import Natural
from integers import Integers
from rational import Rational
from input_create import create_natural, create_integer, create_rational
import copy


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
            Выполнила Котельникова Елизавета гр. 3384
            DEG_P_N
            Функция возвращает степень многочлена
        """
        return self.degree  # возвращает степень многочлена

    def add_pol(self, other):
        """
            Выполнила Конасова Яна гр. 3384
            Add_PP_P.
            Сложение многочленов.
        """
        arr = []
        diff = self.degree.cmp_of_natural_number(other.degree)
        # берем наименьшую степень многочленов
        if diff == 2:
            mini = int(''.join(map(str, other.degree.values)))
        else:
            mini = int(''.join(map(str, self.degree.values)))
        # складываем первые члены многочлены, которые есть у обоих многочленов
        for i in range(mini + 1):
            n = self.coefficients[i].__add__(other.coefficients[i])
            arr.append(n)
        if diff == 2:
            # если первый полином больше, то заполняем остатки из него, просто добавляя в массив
            for i in range(mini + 1, int(''.join(map(str, self.degree.values))) + 1):
                arr.append(self.coefficients[i])
            return Polynomial([self.degree, arr])
        if diff == 1:
            # если больше второй то наоборот
            for i in range(mini + 1, int(''.join(map(str, other.degree.values))) + 1):
                arr.append(other.coefficients[i])
            return Polynomial([other.degree, arr])
        # удаление нулей в конце, так как они ни на что не влияют и портят конечную степень многочлена
        while arr[-1].numerator.values == [0]:
            arr = arr[:-1]
        mini = Natural(len([int(x) for x in str(len(arr) - 1)]), [int(x) for x in str(len(arr) - 1)])
        return Polynomial([mini, arr])

    def multiply_by_monomial(self, k):
        """
            Выполнила Полещук Виолетта гр. 3384
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
        if len(result) != 0 and result[0] == '+':
            result = result[1:]
        return result

    def pol_derivative(self):
        """
            Выполнил Хальзев Александр гр. 3384
            DER_P_P
            Возвращает производную многочлена.
        """
        # глубокое копирование с отбрасыванием последнего коэффициента
        pol = copy.deepcopy(self)
        coeffs = pol.coefficients[1:]
        new_coeffs = []
        # коэффициент для умножения
        deg = create_natural([1])
        for coef in coeffs:
            # алгоритм создания нового коэффициента, в зависимости от его расположения в массиве коэффициентов
            s = coef.numerator.sign
            value = coef.numerator.abs_integer().trans_in_natural().__mul__(deg).values
            Int_coef = Integers(len(value), value, s)
            coef = Rational([Int_coef, coef.denominator])
            new_coeffs.append(coef)
            deg += create_natural([1])

        return Polynomial([pol.degree.__sub__(Natural(1, [1])), new_coeffs])

    def gcf_pol(self, other):
        """
            Выполнила Конасова Яна гр. 3384
            GCF_PP_P
            НОД многочленов.
        """
        # копирование наибольего в pol_1, а меньшего в pol_2
        if self.degree.cmp_of_natural_number(other.degree) == 1:
            pol_1 = other.copy()
            pol_2 = self.copy()
        else:
            pol_1 = self.copy()
            pol_2 = other.copy()
        # если равны, то НОД любой из них
        if pol_1.coefficients == pol_2.coefficients:
            return pol_1
        # находим остаток от деления pol_1 на pol_2 и сохраняем делитель в pol_3
        ost = pol_1.polynomial_remainder(pol_2)
        pol_3 = pol_2
        while ost.coefficients != []:
            # если НОД равен числу, а не полиному, то выводим единицу
            if len(ost.coefficients) == 1:
                return Polynomial([Natural(1, [0]), [Rational([Integers(1, [1], False), Natural(1, [1])])]])
            # сохраняем последний остаток, так как он может быть последним != 0, в ином случае он станет делиммым
            ost1 = ost
            ost = pol_3.polynomial_remainder(ost)

            pol_3 = ost1
            # цикл завершается, когда последний остаток == 0
        return pol_3

    def eliminating_duplicate_roots(self):
        """
            Выполнила Хальзев Александр гр. 3384
            NMR_P_P
            Преобразование многочлена — кратные корни в простые.
        """

        pol = self.copy()
        # Нахождение производной многочлена
        f_der = pol.pol_derivative()
        # Нахождение НОД многочлена
        d = pol.gcf_pol(f_der)
        if d.degree.n == 1 and d.degree.values[0] == 0:
            return pol
        # Выводим результат деления многочлена на d
        return pol.div_polynom(d)

    def leading_coefficient(self):
        """
            Выполнила Прокопович Яна гр. 3384
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
            Выполнила Прокопович Яна гр. 3384
            MUL_PQ_P
            Умножение многочлена на рациональное число
        """
        polynomial = self.copy()
        polynomial.coefficients = [number.__mul__(scalar) for number in polynomial.coefficients]
        return polynomial

    def subtract_polynomial(self, other):
        """
            Выполнила Прокопович Яна гр. 3384
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
            for coef in s_pol.coefficients[len(f_pol.coefficients):]:
                inverted_numerator = coef.numerator.invert_sign()
                new_coef = Rational([inverted_numerator, coef.denominator])
                arr.append(new_coef)
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
            Выполнила Прокопович Яна гр. 3384
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
            Выполнила Прокопович Яна гр. 3384
            MOD_PP_P
            Вычисляет остаток от деления многочлена на многочлен при делении с остатком.
        """
        f_pol = self.copy()
        s_pol = other.copy()
        if f_pol.degree.cmp_of_natural_number(s_pol.degree) == 1:
            return f_pol
        # Выполнение деления многочленов для получения частного
        quotient = f_pol.div_polynom(s_pol)
        # Умножаем частное на делитель, чтобы получить произведение
        product = quotient.__mul__(s_pol)
        # Вычитаем произведение из делимого многочлена, чтобы получить остаток
        remainder = f_pol.subtract_polynomial(product)
        return remainder

    def __mul__(self, other):
        """
            Выполнил Баяндин Дмитрий гр. 3384
            MUL_PP_P
            Умножение многочленов
        """
        # создаем полином для записи ответа
        answer = Polynomial([create_natural([0]), [create_rational(create_integer([0], False), create_natural([1]))]])

        # сделали копии полиномов
        first_pol = self.copy()
        second_pol = other.copy()

        #  перебираем по количеству слагаемых во втором многочлене
        for i in range(len(second_pol.coefficients)):
            if second_pol.coefficients[i].numerator.values != [0]:
                # умножаем первый полином на x^i
                multiply_xi = first_pol.multiply_by_monomial(create_natural([int(j) for j in str(i)]))
                # умножаем первый полином на коэффициент соответсвующий слагаемому степени x^i и прибавляем его к ответу
                answer = answer.add_pol(multiply_xi.multiply_by_scalar(second_pol.coefficients[i]))

        return answer

    def div_polynom(self, other):
        """
            Выполнил Баяндин Дмитрий гр. 3384
            DIV_PP_P
            Частное от деления многочлена на многочлен при делении с остатком
        """
        # если степень второго полинома больше, чем степень первого, частное будет равно 0
        if self.degree.cmp_of_natural_number(other.degree) == 1:
            return Polynomial([create_natural([0]), [create_rational(create_integer([0], False), create_natural([1]))]])

        # сделали копии полиномов
        first_pol = self.copy()
        second_pol = other.copy()

        # создаем полином для записи ответа
        answer = Polynomial([create_natural([0]), [create_rational(create_integer([0], False), create_natural([1]))]])

        # будет делить, пока степень делимого больше или равна степени делителя, либо не равна 0
        while first_pol.degree.cmp_of_natural_number(second_pol.degree) != 1 and first_pol.degree.number_is_not_zero():
            # получаем коэффициент домножения делителя (отношение старших коэффициентов)
            ratio = first_pol.coefficients[-1].division_of_fractions(second_pol.coefficients[-1])
            # прибавляем к результату одночлен, с коэффициентом ratio и степенью равной разности степеней делимого и делителя
            answer = answer.add_pol(
                (Polynomial([create_natural([0]), [ratio]])).multiply_by_monomial(first_pol.degree - second_pol.degree))
            # вычитаем из делимого полином, полученный умножением одночлена на делитель
            first_pol = first_pol.subtract_polynomial(
                second_pol.multiply_by_monomial(first_pol.degree - second_pol.degree).multiply_by_scalar(ratio))
        return answer