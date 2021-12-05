# coding: utf-8
"""
Файл с алгоритмами с возвратом
"""

import random

def conflict(state, col):
    """
    Вспомогательный метод, который определяет не будет ли ферзь угрожать другим
    :param state: статус
    :param col: колонна
    :return: bool
    """
    row = len(state)
    for i in range(row):
        if abs(state[i] - col) in (0, row-i):
            return True
    return False


def queens(num=8, state=()):
    """
    Генератор расстановки ферзей
    :param num: количество ферзей
    :param state: статус
    :return:
    """
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos,) + result


def queenprint(solution):
    """
    Красивый вывод расстановки
    :param solution:
    :return:
    """
    def line(pos, length=len(solution)):
        return '. '*(pos)+'X ' + '. '*(length-pos-1)
    for pos in solution:
        print(line(pos))

if __name__ == '__main__':
    for solution in list(queens(8)):
        print(solution)
    queenprint(random.choice(list(queens())))