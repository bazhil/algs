# coding: utf-8
"""
Файл с криптографическими алгоритмами из книги
"""
import random
from pprint import pprint

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


def mix_columns(text, key):
    """
    Метод который шифрует сообщение и дополнительно перемешивает столбцы таблицы
    :param text: текст
    :param key: ключ шифрования (число, длина которого соответствует числу столбцов в получаемой таблице)
    :return:
    """
    key = str(key)
    table = replacing_crypt(text)
    new_table = []

    # раскладываю число на символы, обхожу
    for i in range(len(key)):
        if int(key[i]) <= len(table):
            new_table.append(table[int(key[i])-1])

    return new_table




if __name__ == '__main__':
    pprint(replacing_crypt('проверка тест шифр обучение'))
    pprint(mix_columns('проверка тест шифр обучение', 2341))