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


def horse(row, col, move_number, num_moves_taken):
    # TODO: проверить и отладить!!!
    # перемещаем коня в эту позицию
    num_moves_taken += 1
    move_number[row, col] = num_moves_taken

    # если конь прошелся по всем клеткам - выходим
    if num_moves_taken == 64:
        return

    # массивы для определения допустимости ходов
    d_rows = [-2, -2, -1, 1, 2, 2, 1, -1]
    d_cols = [-1, 1, 2, 2, 1, -1, -2, -2]

    # пробуем все допустимые позиции для следующего кода
    for i in range(7):
        r = row + d_rows[i]
        c = col + d_cols[i]
        if r >= 0 and r < 6 and c >= 0 and c < 6 and move_number[r, c] == 0:
            if horse(r, c, move_number, num_moves_taken):
                return True

    # этот ход не работает
    move_number[row, col] = 0

    return False




if __name__ == '__main__':
    for solution in list(queens(8)):
        print(solution)
    queenprint(random.choice(list(queens())))