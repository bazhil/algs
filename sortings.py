# coding=utf-8


def insertion_sort(values):
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


if __name__ == '__main__':
    test_list = [9, 8, 55, 7, 2, 0, 568, 3, 4, 11]

    lst = insertion_sort(test_list)
    print(lst)