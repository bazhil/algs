# coding=utf-8
import math


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



if __name__ == '__main__':
    # print(find_factor(1221))
    print(find_factor(5122))