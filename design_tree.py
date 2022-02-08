# coding=utf-8
"""
Алгоритмы деревьев принятия решений
"""

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
