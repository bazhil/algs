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

