# coding=utf-8
"""
Алгоритмы деревьев принятия решений
"""
import random


def minimax(board_position, move, best_value, player_one, player_two, depth, max_depth):
    """
    Алгоритм поиска лучшего хода для игрока №1
    Не ясно как тестировать, тк под каждый параметр напрашивается свой объект и игра, которая их обвязывает в единую логку
    :param board_position: позиция на доске
    :param move: ход
    :param best_value: лучшее значение
    :param player_one: игрок 1
    :param player_two: игрок 2
    :param depth: глубина дерева
    :param max_depth: максимальная глубина дерева
    :return:
    """
    # величина очков для победы (взял с потолка)
    win = 100
    loss = -100
    # Проверяю, не превышена ли максимально допустимая глубина рекурсии
    if depth > max_depth:
        best_value = None
        return

    # Определяю ход, который минимизирует шансы на успех player2
    lowest_value = 0
    lowest_move = None
    # не ясно, сколько будет возможных ходов и что за объект - ход
    for move in range(10):
        # тестовое положение на доске
        test_board_position = 5
        # это выигрыш, проигрыш, или ничья (взял для простоты счастливое число 7)
        if move == 7:
            lowest_move, lowest_value = 1, 1
        # рекурсивно пробуем другие возможные ходы
        else:
            # инициализирую тестовые величины и проверяю, подойдут ли они
            test_value = 1 + move
            test_move = 1 + move
            minimax(test_board_position, test_move, test_value, player_one, player_two, depth, max_depth)
            # если есть лучший ход - сохраняем
            if test_value < lowest_value:
                lowest_value, lowest_move = test_value, test_move

    # сохраняю лучший ход
    best_move = lowest_move

    # преобразую значениу доски для игрока 2 в значения для игрока 1
    if lowest_value == win:
        best_value = loss
    elif lowest_value == loss:
        best_value = win
    else:
        # иные возможные варианты
        pass


def  start_exhausttive_search():
    """
    Запуск полного поиска
    :return:
    """
    # инициализируем лучшее решение, которое заменяет первое тестовое
    exhausttive_search(0)


# хз откуда взялся в книге, добавляю переменную, тк она используется в exhausttive_search
max_index = None


def exhausttive_search(next_index):
    """
    Проверяем, закончили ли мы
    :param next_index:
    :return:
    """
    global max_index
    if next_index == max_index:
        # все элементы назначены, значит, мы в терминальной вершине
        # если тестовое решение лучше, чем последнее найденное - сохраняем его
        max_index = next_index
    else:
        # назначены не все элементы - мы не в терминальной вершине
        # относим элемент к группе 0
        exhausttive_search(next_index + 1)
        # отменяем отнесение элемента к группе 0

        # относим элемент next_index к группе 1
        exhausttive_search(next_index + 1)
        # отменяем отнесение элемента к группе 1


def start_branch_and_bound():
    """
    Инициализирует лучшее решение
    :return:
    """
    branch_and_bound(0)


def branch_and_bound(next_index):
    """
    Метод ветвей и границ
    :param next_index:
    :return:
    """
    global max_index
    if next_index == max_index:
        # все элементы назначены, значит, мы в терминальной вершине
        # если тестовое решение лучше, чем последнее найденное - сохраняем его
        max_index = next_index
    else:
        # назначены не все элементы, мы не в терминальной вершине
        # если тестовое значение не может превзойти текущее лучшее - возвращаемся
        if next_index < max_index:
            return
        # относим элемент к группе 0
        branch_and_bound(next_index + 1)
        # отменяем отнесение элемента к группе 0

        # относим элемент next_index к группе 1
        branch_and_bound(next_index + 1)
        # отменяем отнесение элемента к группе 1


# инициализирую заглушки
num_trails = 1000
indexes = list(range(num_trails))
groups = {0: [],
          1: []}
designs = []

def random_search():
    """
    случайный поиск
    :return:
    """
    # инициализируем лучшее решение, которое заменяет первое тестовое
    for trail in range(num_trails):
        # произвольно относим элемент с номером index в группу 0 или 1
        for index in indexes:
            rand_ind = random.randint(0, 1)
            groups[rand_ind].append(index)

        # проверяем, насколько совершенно это решение
        # если тестовое решение подходит лучше - сохраняем его
        if ((trail + index) * 3) % 2 > 0:
            designs.append(trail)



