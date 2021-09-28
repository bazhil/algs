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


def find_largest(arr):
    """
    Метод определяющий наибольшее число в списке
    :param arr: список натуральных чисел
    :return:
    """
    largest = arr[0]
    for k, v in enumerate(arr):
        if v > largest:
            largest = v

    return largest


def contain_duplicates(arr):
    """
    Метод, определяющий, содержит ли список дубликаты
    :param arr: список натуральных чисел
    :return:
    """
    for k, v in enumerate(arr):
        for e, d in enumerate(arr):
            if v == d and k != e:
                return True

    return False


def contain_duplicates_2(arr):
    """
    Еще один метод, определяющий, содержит ли список дубликаты
    :param arr: список натуральных чисел
    :return:
    """
    return True if len(arr) > len(set(arr)) else False


if __name__ == '__main__':
    # print(GCD(1220, 5))
    # print(find_largest(list(range(15))))
    print(contain_duplicates_2([1, 2, 3, 4, 6, 7, 5, 5]))