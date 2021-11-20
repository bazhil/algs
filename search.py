# coding=utf-8


def linear_search(values: list, target) -> int:
    """
    Алгоритм линейного поиска O(N)
    :param values: список значений
    :param target: искомое значение
    :return:
    """
    for i in values:
        if i == target:
            return values.index(i)
        if i > target:
            return -1
    return -1


def binary_search(values:list, target:int ) -> int:
    """
    Бинарный поиск
    :param values: список значений
    :param target: искомое значение
    :return:
    """
    min = 0
    max = len(values) - 1

    while min < max:
        mid = (max + min) // 2
        if target < values[mid]:
            max = mid - 1
        elif target > values[mid]:
            min = mid + 1
        else:
            return mid
    return -1


def interpolation_search(values:list, target:int) -> int:
    """
    Интерполяционный поиск
    :param values: список значений
    :param target: искомое значение
    :return:
    """
    min, max = 0, len(values) - 1
    while min < max:
        mid = int(min + (max - min) * (target - values[min]) / (values[max] - values[min]))
        if values[mid] == target:
            return mid
    return -1



if __name__ == '__main__':
    test_list = [i for i in list(range(12324342)) if i % 17 == 0]
    ind1 = linear_search(test_list, 34)
    print(ind1, test_list[ind1])
    ind2 = binary_search(test_list, 170)
    print(ind2, test_list[ind2])
    ind3 = interpolation_search(test_list, 340)
    print(ind3, test_list[ind3])