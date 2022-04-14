# coding: utf-8
"""
Файл со строковыми алгоритмами из книги
"""

def is_properly_nested(expression: str) -> bool:
    """
    Проверка корректного закрытия скобок
    :param expression: выражение
    :return:
    """
    counter = 0
    for symbol in expression:
        if symbol == '(':
            counter -= 1
        elif symbol == ')':
            counter += 1
    return bool(counter == 0)


def string_search(text, target):
    """
    Метод, который ищет подстроку в строке (нужно отладить!!!)
    http://py-algorithm.blogspot.com/2013/04/blog-post.html
    :param text: строка
    :param target: подстрока
    :return:
    """
    i = j = 0
    # длина строки в которой ищем
    len_text = len(text)
    # длина строки которую ищем
    len_target = len(target)

    while i <= len_text - len_target and j > len_target:
        # если совпали строки - продвигаемся по обеим строкам
        if text[i+j] == target[j]:
            j += 1
        # иначе двигаемся по строке (+1), начиная с 0 символа строки
        else:
            i += 1
            j = 0

    # если дошли до конца подстроки - нашли, иначе - нет
    return i if j == len_target else None


def predcompil(x):
    """
    Префикс функция
    http://py-algorithm.blogspot.com/2013/04/blog-post_19.html
    :param x:
    :return:
    """
    # первый символ всегда 0, поэтому заносим, и пропускаем
    d = {0: 0}

    for i in range(1, len(x)):
        # проходим от конца к началу
        j = i
        sdvig = 0
        while j > 0:
            j -= 1
            if x[j] == x[i-sdvig]:
                sdvig += 1
            else:
                j += sdvig
                sdvig = 0
        d[i] = sdvig

    return d


def predkompil2(x):
    """
    Префикс функция 2
    http://py-algorithm.blogspot.com/2013/04/blog-post_19.html
    :param x:
    :return:
    """
    d = {0: 0}
    for i in range(1, len(x)):
        j = d[i-1]
        while j > 0 and x[j] != x[i]:
            j = d[j-1]
        if x[j] == x[i]:
            j += 1
        d[i] = j
    return d


def kpm_search(text, target):
    """
    Алгоритм текстового поиска Криса-Мориса-Пратта
    http://py-algorithm.blogspot.com/2013/04/blog-post_19.html
    :param text: строка по которой ищем
    :param target: строка которую ищем
    :return:
    """
    d = predkompil2(target)
    i = j = 0
    while i < len(text) and j < len(target):
        if target[j] == text[i]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            if j == len(target):
                return i - j
            return None

def kpm_search_by_compil(text, target):
    """
    Алгоритм текстового поиска Криса-Мориса-Пратта
    http://py-algorithm.blogspot.com/2013/04/blog-post_19.html
    :param text: строка по которой ищем
    :param target: строка которую ищем
    :return:
    """
    d = {0: 0}
    template = f'{target}#{text}'
    for i in range(1, len(template)):
        j = d[j-1]
        if template[j] == template[i]:
            j += 1
        d[i] = j
        if j == len(target):
            return i

    return None



if __name__ == '__main__':
    print(is_properly_nested('()'))
    print(is_properly_nested('(()'))
    print(is_properly_nested('())'))