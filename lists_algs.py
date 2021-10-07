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


if __name__ == '__main__':
    iterate([1,2,3,4,5])