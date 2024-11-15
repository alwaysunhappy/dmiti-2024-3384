from natural import Natural
from integers import Integers
from rational import Rational
from polynomial import Polynomial
from input_create import *


class Launch:
    def __init__(self, number):
        self.number = number

    def start_function(self):
        if self.number == 0:
            print("Чтобы запустить функцию нужно ввести число от 1 до 45, где каждый номер означает функцию.")
            print("1 - Сравнение натуральных чисел")
            print("2 - Проверка на ноль")
            print("3 - Добавление 1 к натуральному числу")
            print("4 - Сложение натуральных чисел")
            print("5 - Вычитание из первого большего натурального числа второго меньшего или равного")
            print("6 - Умножение натурального числа на цифру")
            print("7 - Умножение натурального числа на 10^k, k-натуральное")
            print("8 - Умножение натуральных чисел")
            print("9 - Вычитание из натурального другого натурального, умноженного на цифру для случая с "
                  "неотрицательным результатом")
            print("10 - Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k,"
                  "где k - номер позиции этой цифры (номер считается с нуля)")
            print("11 - Неполное частное от деления первого натурального числа на второе с остатком (делитель отличен "
                  "от нуля)")
            print("12 - Остаток от деления первого натурального числа на второе натуральное (делитель отличен от нуля)")
            print("13 - НОД натуральных чисел")
            print("14 - НОК натуральных чисел")
            print("15 - Абсолютная величина числа")
            print("16 - Определение положительности числа")
            print("17 - Умножение целого числа на (-1)")
            print("18 - Преобразование натурального числа в целое")
            print("19 - Преобразование целого неотрицательного числа в натуральное")
            print("20 - Сложение целых чисел")
            print("21 - Вычитание целых чисел")
            print("22 - Умножение целых чисел")
            print("23 - Нахождение частного от деления целого на целое (делитель отличен от нуля)")
            print("24 - Нахождение остатка от деления целого на целое (делитель отличен от нуля)")
            print("25 - Сокращение дроби")
            print("26 - Проверка сокращенного дробного на целое")
            print("27 - Преобразование целого числа в дробное")
            print("28 - Преобразование сокращенного дробного в целое")
            print("29 - Сложение дробей")
            print("30 - Вычитание дробей")
            print("31 - Умножение дробей")
            print("32 - Деление дробей")
            print("33 - Сложение многочленов")
            print("34 - Вычитание многочленов")
            print("35 - Умножение многочлена на рациональное число")
            print("36 - Умножение многочлена на x^k")
            print("37 - Нахождение старшего коэффициента многочлена")
            print("38 - Нахождение степени многочлена")
            print("39 - Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей")
            print("40 - Умножение многочленов")
            print("41 - Частное от деления многочлена на многочлен при делении с остатком")
            print("42 - Остаток от деления многочлена на многочлен при делении с остатком")
            print("43 - Нахождение НОД многочленов")
            print("44 - Нахождение производной многочлена")
            print("45 - Преобразование многочлена — кратные корни в простые")

        if self.number == 1:
            natural = input_natural()
            natural_second = input_natural()
            print(natural.cmp_of_natural_number(natural_second))

        if self.number == 2:
            natural = input_natural()
            print(natural.number_is_not_zero())

        if self.number == 3:
            natural = input_natural()
            print(natural.increment())

        if self.number == 4:
            natural = input_natural()
            natural_second = input_natural()
            print(natural.__add__(natural_second))

        if self.number == 5:
            natural = input_natural()
            natural_second = input_natural()
            print(natural.__sub__(natural_second))

        if self.number == 6:
            natural = input_natural()
            number = int(input("Введите цифру: "))
            print(natural.multiplication_by_digit(number))

        if self.number == 7:
            natural = input_natural()
            k = input_natural()
            print(natural.multiply_by_ten(k))

        if self.number == 8:
            natural = input_natural()
            natural_second = input_natural()
            print(natural.__mul__(natural_second))

        if self.number == 9:
            natural = input_natural()
            natural_second = input_natural()
            k = int(input("Введите цифру: "))
            print(natural.subtract_scaled_natural(natural_second, k))

        if self.number == 10:
            natural = input_natural()
            natural_second = input_natural()
            print(natural.first_digit__of_scaled_division(natural_second))

        if self.number == 11:
            natural = input_natural()
            natural_second = input_natural()
            print(natural.div_natural(natural_second))

        if self.number == 12:
            natural = input_natural()
            natural_second = input_natural()
            print(natural.mod_natural(natural_second))

        if self.number == 13:
            natural = input_natural()
            natural_second = input_natural()
            print(natural.gcf_natural(natural_second))

        if self.number == 14:
            natural = input_natural()
            natural_second = input_natural()
            print(natural.lmc_natural(natural_second))

        if self.number == 15:
            integer = input_integer()
            print(integer.abs_integer())

        if self.number == 16:
            integer = input_integer()
            print(integer.check_sign())

        if self.number == 17:
            integer = input_integer()
            print(integer.invert_sign())

        if self.number == 18:
            integer = input_integer()
            print(integer.trans_in_integer())

        if self.number == 19:
            integer = input_integer()
            print(integer.trans_in_natural())

        if self.number == 20:
            integer = input_integer()
            integer_second = input_integer()
            print(integer.__add__(integer_second))

        if self.number == 21:
            integer = input_integer()
            integer_second = input_integer()
            print(integer.__sub__(integer_second))

        if self.number == 22:
            integer = input_integer()
            integer_second = input_integer()
            print(integer.__mul__(integer_second))

        if self.number == 23:
            integer = input_integer()
            integer_second = input_integer()
            print(integer.div_integer(integer_second))

        if self.number == 24:
            integer = input_integer()
            integer_second = input_integer()
            print(integer.mod_integer(integer_second))

        if self.number == 25:
            fraction = input_rational()
            print(fraction.fraction_reduction())

        if self.number == 26:
            fraction = input_rational()
            print(fraction.int_check())

        if self.number == 27:
            integer = input_integer()
            print(integer.trans_in_rational())

        if self.number == 28:
            fraction = input_rational()
            print(fraction.trans_in_integer())

        if self.number == 29:
            fraction = input_rational()
            fraction_second = input_rational()
            print(fraction.__add__(fraction_second))

        if self.number == 30:
            fraction = input_rational()
            fraction_second = input_rational()
            print(fraction.sub_rat(fraction_second))

        if self.number == 31:
            fraction = input_rational()
            fraction_second = input_rational()
            print(fraction.__mul__(fraction_second))

        if self.number == 32:
            fraction = input_rational()
            fraction_second = input_rational()
            print(fraction.division_of_fractions(fraction_second))

        if self.number == 33:
            polynomial = input_polynomial()
            polynomial_second = input_polynomial()
            print(polynomial.add_pol(polynomial_second))

        if self.number == 34:
            polynomial = input_polynomial()
            polynomial_second = input_polynomial()
            print(polynomial.subtract_polynomial(polynomial_second))

        if self.number == 35:
            polynomial = input_polynomial()
            fraction = input_rational()
            print(polynomial.multiply_by_scalar(fraction))

        if self.number == 36:
            polynomial = input_polynomial()
            k = input_natural()
            print(polynomial.multiply_by_monomial(k))

        if self.number == 37:
            polynomial = input_polynomial()
            print(polynomial.leading_coefficient())

        if self.number == 38:
            polynomial = input_polynomial()
            print(polynomial.degree_polynomial())

        if self.number == 39:
            polynomial = input_polynomial()
            print(polynomial.factor_polynomial())

        if self.number == 40:
            polynomial = input_polynomial()
            polynomial_second = input_polynomial()
            print(polynomial.__mul__(polynomial_second))

        if self.number == 41:
            polynomial = input_polynomial()
            polynomial_second = input_polynomial()
            print(polynomial.div_polynom(polynomial_second))

        if self.number == 42:
            polynomial = input_polynomial()
            polynomial_second = input_polynomial()
            print(polynomial.polynomial_remainder(polynomial_second))

        if self.number == 43:
            polynomial = input_polynomial()
            polynomial_second = input_polynomial()
            print(polynomial.gcf_pol(polynomial_second))

        if self.number == 44:
            polynomial = input_polynomial()
            print(polynomial.pol_derivative())

        if self.number == 45:
            polynomial = input_polynomial()
            print(polynomial.eliminating_duplicate_roots())


if __name__ == "__main__":
    print("Для вывода справки введите 0.")
    a = int(input("Введите номер функции: "))
    Launch(a).start_function()
