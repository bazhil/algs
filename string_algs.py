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


if __name__ == '__main__':
    print(is_properly_nested('()'))
    print(is_properly_nested('(()'))
    print(is_properly_nested('())'))