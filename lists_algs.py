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


if __name__ == '__main__':
    # iterate([1,2,3,4,5])
    # print(find_cell_before([123,22,1,2,3,19,4,55,5,6,7,8,9], 123))
    print(selection_sort([123,22,1,2,3,19,4,55,5,6,7,8,9]))
