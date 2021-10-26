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


def bubble_sort(values):
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




if __name__ == '__main__':
    test_list = [9, 8, 55, 7, 2, 0, 568, 3, 4, 11]

    # ins_lst = insertion_sort(test_list)
    # print(ins_lst)
    bbl_lst = bubble_sort(test_list)

    print(bbl_lst)

