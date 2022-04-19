# coding: utf-8
"""
Файл с криптографическими алгоритмами из книги
"""
import random

table = [[], [], [], []]


def replacing_crypt(text):
    """
    перестановка шифрованием
    :param text: тест для шифрования
    :return:
    """
    index = 0
    num_rows = 4
    num_cols = len(text)//num_rows
    # инициализирую таблицу для раскладывания символов
    table = [[] for i in range(num_rows)]
    print(table)
    for col in range(num_cols):
        for row in range(num_rows):
            # если натыкаемся на пробел, то заменяем рандомным числом
            if text[index] != ' ':
                table[row].append(text[index])
            else:
                table[row].append(random.randint(0, 9))
            index += 1

    return table


if __name__ == '__main__':
    print(replacing_crypt('проверка тест шифр обучение'))