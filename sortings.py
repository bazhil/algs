# coding=utf-8
import random


def insertion_sort(values: list) -> list:
    """
    Сортировка вставкой O(N**2)
    :param values: список чисел
    :return:
    """
    for i in range(1, len(values)):
        for j in range(len(values)):
            if j < i and values[j] > values[i]:
                values[j], values[i] = values[i], values[j]

    return values


def bubble_sort(values: list) -> list:
    """
    Пузырьковая сортировка O(N**2)
    :param values: список чисел
    :return:
    """
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(1, len(values)):
            if values[i] < values[i-1]:
                values[i], values[i-1] = values[i-1], values[i]
                not_sorted = True

    return values


def heapify(values: list, size: int, root: int):
    """
    Преобразование списка в кучу
    :param values: список чисел
    :param size: размер списка
    :param root: корневой элемент списка
    :return:
    """
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    # проверяем, существует ли левый дочерний элемент, больший, чем корень
    if left < size and values[root] < values[left]:
        largest = left

    # проверяем, существует ли правый дочерний элемент, больший, чем корени
    if right < size and values[largest] < values[right]:
        largest = right

    if largest != root:
        values[root], values[largest] = values[largest], values[root]
        heapify(values, size, root)


def heap_sort(values):
    """
    Сортировка кучей
    :param values: список чисел
    :return:
    """
    n = len(values)

    # построение max-heap
    for i in range(n, -1, -1):
        heapify(values, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        values[i], values[0] = values[0], values[i]
        heapify(values, i, 0)

    return values


def quick_sort(values: list) -> list:
    """
    Быстрая сортировка Хоара (O(N*log N))
    :param values: список чисел
    :return:
    """
    if len(values) <= 1:
        return values
    else:
        rand = random.choice(values)
        s_vals = [v for v in values if v < rand]
        m_vals = [v for v in values if v > rand]
        e_vals = [v for v in values if v == rand]

        return quick_sort(s_vals) + e_vals + quick_sort(m_vals)


def merge_sort(values: list, start: int, end: int):
    """
    Сортировка слиянием
    :param values: список чисел
    :param start: начало
    :param end: конец
    :return:
    """
    if start >= end:
        return

    middle = (start + end) // 2
    merge_sort(values, start, middle)
    merge_sort(values, middle + 1, end)
    merge(values, start, end, middle)


def merge(values, start, end, middle):
    """
    Метод объединяющий подсписки
    :param values: список чисел для сортировки
    :param start: начало
    :param end: конец
    :param middle: середина
    :return:
    """
    # создаем подсписки
    left_sublist = values[start:middle + 1]
    right_sublist = values[middle + 1:end + 1]

    # переменные для прослеживания хода сортировки
    left_sublist_index = 0
    right_sublist_index = 0
    sorted_index = start

    # сортируем подсписки
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:
            values[sorted_index] = left_sublist[left_sublist_index]
            left_sublist_index = left_sublist_index + 1
        else:
            values[sorted_index] = right_sublist[right_sublist_index]
            right_sublist_index = right_sublist_index + 1

        sorted_index = sorted_index + 1

    while left_sublist_index < len(left_sublist):
        values[sorted_index] = left_sublist[left_sublist_index]
        left_sublist_index = left_sublist_index + 1
        sorted_index = sorted_index + 1

    while right_sublist_index < len(right_sublist):
        values[sorted_index] = right_sublist[right_sublist_index]
        right_sublist_index = right_sublist_index + 1
        sorted_index = sorted_index + 1


def counting_sort(values: list, max_value: int):
    """
    Сортировка подсчетом
    :param values: список чисел
    :param max_value: максимальное значение
    :return:
    """
    # инициалищируем счетчик
    c = [0]*(max_value + 1)
    for i in range(len(values)):
        c[values[i]] += 1

    # получаем индексы
    c[0] = c[0] - 1
    for i in range(1, max_value + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(values)

    # для стабильной сортировки делаем реверс списка
    for x in reversed(values):
        result[c[x]] = x
        c[x] = c[x] - 1

    return result


if __name__ == '__main__':
    test_list = [9, 8, 55, 7, 2, 0, 568, 3, 4, 11]
    print(test_list)
    # ins_lst = insertion_sort(test_list)
    # print(ins_lst)
    # bbl_lst = bubble_sort(test_list)
    # print(bbl_lst)
    # heap_list = make_heep(test_list)
    # print(heap_list)

    # top = remove_heap_top(test_list)
    # print(top)
    # heap_top = remove_heap_top(heap_list)
    # print(heap_top)
    # sorted_by_heap = heap_sort(test_list)
    # print(sorted_by_heap)

    # print(quick_sort(test_list))
    # merge_sort(test_list, 0, len(test_list) - 1)



    print(counting_sort(test_list, max(test_list)))