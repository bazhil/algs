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
    return bool(len(arr) > len(set(arr)))


def contain_duplicates_3(arr):
    """
    Очередной метод, определяющий, содержит ли список дубликаты
    :param arr: список натуральных чисел
    :return:
    """
    for k, v in enumerate(arr):
        if k == len(arr) - 1:
            return False
        if v == arr[k+1]:
            return True


def dividing_point(arr):
    """
    метод, который грубо определяет среднее значение в массиве.
    работает за O(1)
    :param arr: список натуральных чисел
    :return:
    """
    n1 = arr[0]
    n2 = arr[-1]
    n3 = arr[arr.index(n2)//2]
    if n1 < n2 and n2 < n3:
        return n1
    if n2 < n1 and n3 < n3:
        return n2
    return n3


def fib():
    """
    Первый способ рассчета чисел Фибоначчи
    :return:
    """
    prew = cur = 1
    element = input('Введите номер искомого элемента: ')
    element = int(element)
    i = 0
    for n in range(int(element - 2)):
        tmp = prew + cur
        prew = cur
        cur = tmp
        i += 1

        print(str(i) + ' элемент последовательности равен ' + str(cur))



# def find_item(target_value):
#     """
#     Метод, который ищет значение в куче / дереве
#     :param target_value: искомое значение
#     :return:
#     """
#     # TODO: позже составить дерево и проверить как работает алгоритм -> разобраться со свойствами
#     test_node = 0
#
#     while True:
#         if test_node == None:
#             return
#         if target_value == test_node.Value():
#             return test_node
#         elif target_value < test_node.Value():
#             test_node.LeftChild()
#         else:
#             test_node = test_node.RightChild()


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 6, 7, 5, 5, 5, 6, 8, 10]
    arr2 = [1, 2, 3, 4, 6, 7, 5, 5]
    # print(GCD(1220, 5))
    # print(find_largest(list(range(15))))
    # print(contain_duplicates_2(arr2))
    # print(contain_duplicates_3(arr2))
    # print(dividing_point(arr))
    # print(dividing_point(arr2))
    # fib()