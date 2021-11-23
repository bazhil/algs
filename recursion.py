# coding=utf-8
"""
Файл с алгоритмами использующими рекурсию
"""

def factorial(value: int) -> int:
    """
    Метод рассчета факториала заданного числа
    :param value: натуральное число
    :return:
    """
    if value <= 0:
        return 1
    return value * factorial(value - 1)


def fibonacci(value: int) -> int:
    """
    Генератор чисел Фибоначчи (медленный для больших чисел)
    :param value: натуральное число
    :return:
    """
    cur = 1
    if value > 2:
        cur = fibonacci(value - 1) + fibonacci(value - 2)
    return cur

if __name__ == '__main__':
    # print(factorial(5))
    print(fibonacci(12))
