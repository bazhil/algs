# coding=utf-8


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


def make_heep(values: list) -> list:
    """
    Метод, который превращает список в кучу (не уверен, что все верно)
    :param values: список чисел
    :return:
    """
    for i in range(len(values)):
        ind = i
        while ind != 0:
            parent = int((ind - 1) / 2)
            if values[ind] <= values[parent]:
                break
            values[ind], values[parent] = values[parent], values[ind]
            ind = parent

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


if __name__ == '__main__':
    test_list = [9, 8, 55, 7, 2, 0, 568, 3, 4, 11]
    print(test_list)
    # ins_lst = insertion_sort(test_list)
    # print(ins_lst)
    # bbl_lst = bubble_sort(test_list)
    # print(bbl_lst)
    heap_list = make_heep(test_list)
    print(heap_list)

    # top = remove_heap_top(test_list)
    # print(top)
    # heap_top = remove_heap_top(heap_list)
    # print(heap_top)
    sorted_by_heap = heap_sort(test_list)
    print(sorted_by_heap)
