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




if __name__ == '__main__':
    # print(find_factor(1221))
    # print(find_factor(5122))
    # print(find_primes(56))
    # print(is_primitive(710, 10))
    for i in find_primes_2(13, 10):
        print(i)