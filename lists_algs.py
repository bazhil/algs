# coding=utf-8

def iterate(lst):
    """
    Бессмысленный для python алгоритм, но зато из книги
    :param lst: список со значениями
    :return:
    """
    top = lst[0] if lst else None
    for i in range(len(lst)):
        print(top)
        if len(lst) > i + 1:
            top = lst[i+1]


def find_cell_before(lst: list, value):
    """
    Алгоритм, который находит номер ячейки, идущей перед ячейкой в которой лежит переданное в данный метод значение
    :return:
    """
    if value not in lst:
        return None
    i = 0
    while lst[i] != None:
        if lst[i] == value:
            return lst.index(value)
        i += 1


def selection_sort(lst: list) -> list:
    """
    Сортировка выбором
    :param lst: список чисел
    :return:
    """
    for i in range(0, len(lst) - 1):
        smallest = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[smallest]:
                smallest = j
        lst[i], lst[smallest] = lst[smallest], lst[i]

    return lst


def find_element(lst: list, num: int):
    """
    Бессмысленный на питоне алгоритм, который ищет элемент в массиве
    :param lst: список чисел
    :param ind: индекс
    :return:
    """
    for i in range(len(lst)):
        if lst[i] == num:
            return i
    return -1


def find_min(int_lst: list) -> int:
    """
    Алгоритм поиска минимального числа в списке
    :param int_lst: список чисел
    :return:
    """
    min = int_lst[0]
    for i in range(len(int_lst)):
        if int_lst[i] < min:
            min = int_lst[i]

    return min


def find_max(int_arr: list) -> int:
    """
    поиск максимального элемента в массиве
    :param int_arr: массив чисел
    :return:
    """
    max = int_arr[0]
    for i in range(len(int_arr)):
        if int_arr[i] > max:
            max = int_arr[i]

    return max


def find_average(int_lst: list) -> int:
    """
    Алгоритм нахождение среднего арифметического из списка чисел
    :param int_lst:
    :return:
    """
    total = 0
    for i in int_lst:
        total += i

    return total / len(int_lst)


def find_median(int_lst: list) -> int:
    """
    алгоритм нахождения медианного значения (нестабильный, нужно дорабатывать)
    :param int_lst: список чисел
    :return:
    """
    for k1, v1 in enumerate(int_lst):
        larger = 0
        smaller = 0
        for k2, v2 in enumerate(int_lst):
            if v2 < v1:
                smaller += 1
            if v2 > v1:
                larger += 1
        if larger == smaller:
            return v1


def insert_item(lst: list, value: int, position: int) -> list:
    """
    Бессмысленный на питоне алгоритм для вставки элемента в заданную позицию
    :param lst: список
    :param value: переменная
    :param position: позиция вставки
    :return:
    """
    if position + 1 > len(lst):
        return
    for i in lst[len(lst)-1:position+1]:
        lst[i] = lst[i-1]

    lst[position] = value

    return lst


def delete_item(lst: list, position: int) -> list:
    """
    Бессмысленный на питоне алгоритм для вставки элемента в заданную позицию
    :param lst: список
    :param position: позиция вставки
    :return:
    """
    lst = lst[:position] + lst[position+1:]

    return lst


def add_arrays(arr1: list, arr2: list) -> list:
    """
    Алгоритм сложения двух матриц
    :param arr1: список 1 (матрица)
    :param arr2: список 2 (матрица)
    :return: результирующий список
    """
    result = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            new_list = list(map(lambda x, y: x + y, arr1[i], arr2[j]))
            result.append(new_list)

    return result


def multiple_arrays(arr1: list, arr2: list) -> list:
    """
    Умножение двух равноразмерных (!!!) матриц
    :param arr1: список 1 (матрица)
    :param arr2: список 2 (матрица)
    :return:
    """
    result = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            new_list = list(map(lambda x, y: x * y, arr1[i], arr2[j]))
            result.append(new_list)

    return result


if __name__ == '__main__':
    # iterate([1,2,3,4,5])
    # print(find_cell_before([123,22,1,2,3,19,4,55,5,6,7,8,9], 123))
    # print(selection_sort([123,22,1,2,3,19,4,55,5,6,7,8,9]))
    # print(find_element([123, 22, 1, 2, 3, 19, 4, 55, 5, 6, 7, 8, 9], 1))
    # print(find_min([123, 22, 2, 3, 19, 4, 55, 5, 6, 7, 8, 9]))
    # print(find_max([123, 22, 2, 3, 19, 4, 55, 5, 6, 7, 8, 9]))
    # print(find_average([123, 22, 2, 3, 19, 4, 55, 5, 6, 7, 8, 9]))
    # print(find_median([123, 22, 2, 3, 19, 4, 55, 5, 6, 7, 8, 9]))
    # print(insert_item([123, 22, 5, 6, 7, 8, 9], 1111, 7))
    # print(delete_item([123, 22, 5, 6, 7, 8, 9], 0))
    # print(add_arrays([[1,2,3], [11, 22, 33]], [[4, 5, 6], [44, 55, 66]]))
    # print(multiple_arrays([[1,2,3], [11, 22, 33]], [[4, 5, 6], [44, 55, 66]]))