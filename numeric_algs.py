# coding=utf-8
import math
import random


def find_factor(number):
    """
    Метод, который находит простые множители
    :param number:
    :return:
    """
    factors = []
    i = 2
    while i < number:
        while number % i == 0:
            factors.append(i)
            number = number / i
        i += 1
    if number > 1:
        factors.append(number)

    return list(set(factors))


def find_factors(number):
    """
    Метод, который находит простые множители. Работает значительно быстрее предыдущего.
    :param number:
    :return:
    """
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number /= 2

    i = 3
    max_factor = math.sqrt(number)
    while i <= max_factor:
        while number % i == 0:
            factors.append(i)
            number /= i
            max_factor = number ** 0.5 #то же самое, что и math.sqrt()
        i += 2
    if number > 1:
        factors.append(number)

    return factors


def find_primes(max_number):
    """
    Метод, который находит простое число "Решето Эратосфена"
    :param max_number: максимальное число
    :return:
    """
    # составляем список составных чисел
    is_composite = []
    i = 4
    while i <= max_number:
        is_composite.append(i)
        i += 2

    next_prime = 3
    stop_as = max_number ** 0.5

    while next_prime <= stop_as:
        j = next_prime * 2
        while j < max_number:
            if j not in is_composite:
                is_composite.append(j)
            j += next_prime
            next_prime += 2
            if next_prime <= max_number and next_prime in is_composite:
                next_prime += 2

    # собираем список чисел, не входящих в первый список
    primes = []
    k = 2
    while k <= max_number:
        if k not in is_composite:
            primes.append(k)
        k += 1

    return primes


def is_primitive(num: int, max_tests: int):
    """
    Тест, который определяет является ли число простым. Вероятностный алгоритм.
    :param num: тестируемое число
    :param max_tests: максимальное количество тестов
    :return:
    """
    for i in list(range(max_tests)):
        n = random.randint(1, max_tests)
        if n**(num-1) % num != 1:
            return False

    return True


def find_primes_2(num: int, tests: int):
    """
    Алгоритм выбора простых чисел из списка
    :param nums:
    :param tests:
    :return:
    """
    for i in list(range(num)):
        if i >= 1 and is_primitive(i, 10):
            yield i


def use_rectangle_rule(func, xmin, xmax, num_intervals):
    """
    Функция, реализующая формулу прямоугольников, для нахождения площади под графиком функции.
    :param func: функция
    :param xmin: минимальное значение параметра
    :param xmax: максимальное значение параметра
    :param num_intervals: количество интервалов (чем больше, тем меньше погрешность)
    :return:
    """
    # вычисляем ширину прямоугольника
    dx = (xmax - xmin) / num_intervals

    # добавляем области прямоугольников
    total_area = 0
    x = xmin
    i = 1
    while i <= num_intervals:
        total_area += dx * func(x)
        x += dx
        i += 1

    return total_area


def trapezoid_rule(func, xmin, xmax, num_intervals):
    """
    Функция, использующая формулу трапеции
    :param func: функция
    :param xmin: минимальное значение параметра
    :param xmax: максимальное значение параметра
    :param num_intervals: количество интервалов
    :return:
    """
    # вычисляем ширину трапеции
    dx = (xmax - xmin) / num_intervals

    total_area = 0
    x = xmin
    i = 1
    while i <= num_intervals:
        total_area += dx * (func(x) + func(x + dx)) / 2
        x += dx
        i += 1

    return total_area


def slice_area(func, x1, x2, max_slice_error):
    """
    Возвращает площадь заданной области
    :param func: функция
    :param x1: значение параметра
    :param x2: значение параметра
    :param max_slice_error:
    :return: максимальная ошибка
    """
    # вычисляем значение функции на конечных и центральной точках
    y1 = func(x1)
    y2 = func(x2)
    xm = (x1 + x2) / 2
    ym = func(xm)

    # вычисляем площадь большой трапеции и двух меньших трапеций
    area12 = (x2 - x1) * (y1 + y2) / 2
    area1m = (xm - x1) * (y1 + ym) / 2
    aream2 = (x2 - xm) * (ym + y2) / 2
    area1m2 = area1m + aream2

    error = (area1m2 - area12) / area12

    # если погрешность приемлемая возвращаем полученный результат
    if abs(error) < max_slice_error:
        return area1m2

    # делим трапецию и делим еще раз
    return slice_area(func, x1, xm, max_slice_error) + slice_area(func, xm, x2, max_slice_error)


def adaprive_integrate_midpoint(func, xmin, xmax, num_intervals, max_slice_error):
    """
    Функция, использующая адаптивную формулу трапеции
    :param func: функция
    :param xmin: минимальное значение параметра
    :param xmax: максимальное значение параметра
    :param num_intervals: количество интервалов
    :param max_slice_error: максимальная ошибка
    :return:
    """
    # вычисляем ширину трапеции
    dx = (xmax - xmin) / num_intervals

    total_area = 0
    x = xmin
    i = 1
    while i <= num_intervals:
        total_area += slice_area(func, x, x+dx, max_slice_error)
        x += dx
        i += 1

    return total_area


def find_zero(func, dfdx, initial_guess, max_error):
    """
    Метод Ньютона - поиск пересечения оси абцисс с помощью касетельных
    :param func: функция
    :param dfdx: производная функции
    :param initial_guess: начальное приближение
    :param max_error: максимальная ошибка
    :return:
    """
    x = initial_guess

    i = 0
    while i < 100:
        y = func(x)
        if abs(y) < max_error:
            break
        x = x - y / dfdx(x)
        i += 1

    return x


if __name__ == '__main__':
    # print(find_factor(1221))
    # print(find_factor(5122))
    # print(find_primes(56))
    # print(is_primitive(710, 10))

    # for i in find_primes_2(13, 10):
    #     print(i)

    # print(use_rectangle_rule(lambda x: 12*x, 0, 5, 10))
    # print(trapezoid_rule(lambda x: 12*x, 0, 5, 10))
    # print(adaprive_integrate_midpoint(lambda x: 12*x, 0, 5, 5, 1))


