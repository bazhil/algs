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


def find_target(text, target):
    """
    Метод, который ищет подстроку в строке (нужно отладить!!!)
    :param text: строка
    :param target: подстрока
    :return:
    """

    for i in range(len(text)):
        found = True
        # проверяем, начинается ли подстрока с позиции i
        for j in range(len(target)):
            # TODO: тут внимательнее с индексами!
            if text[i] != target[j]:
                found = False
        # если нашли - возвращаем позицию подстроки в тексте
        if found:
            return i

    return -1


if __name__ == '__main__':
    print(is_properly_nested('()'))
    print(is_properly_nested('(()'))
    print(is_properly_nested('())'))