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


if __name__ == '__main__':
    print(is_properly_nested('()'))
    print(is_properly_nested('(()'))
    print(is_properly_nested('())'))