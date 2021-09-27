# coding: utf-8


def GCD(a, b):
    """
    Алгоритм поиска наибольшего общего делителя
    :param a: int
    :param b: int
    :return: delimetr
    """
    while b != 0:
        reminder = a % b
        a = b
        b = reminder

    return a


if __name__ == '__main__':
    print(GCD(1220, 5))
