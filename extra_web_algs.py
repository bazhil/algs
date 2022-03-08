# coding: utf-8

from .graph_algs import GraphNode
from .enqueue import Enqueue

# инициализирую граф
node = GraphNode()

# список упорядоченных узлов
ordered_nodes = []

def extend_partial_ordering(node):
    """
    Упорядочивает узлы
    :param node: стартовый узел
    :return:
    """
    # пока в сети есть узлы рекурсивно обходим и собираем список упорядоченных узлов
    for node in node.neighbors:
        # находим узел без предварительных требований
        ready_node = node.neighbors.pop()
        if ready_node == None:
            return None
        # помещаю узел в итоговый список
        ordered_nodes.append(ready_node)
        extend_partial_ordering(node)


def upgrated_extend_partial_ordering(node):
    """
    Усовершенствованное упорядочивание
    :return:
    :param node: стартовый узел
    """
    # список узлов без предварительных условий
    ready = []

    for node in node.neighbors:
        # находим узел без предварительных требований
        ready_node = node.neighbors.pop()
        if ready_node:
            ready.append(ready_node)
    # пока в списке ready содержатся элементы
    while ready:
        node = ready.pop()
        ordered_nodes.append(node)

        for link in node.links:
            # делаем вид, что появилось новое свойство - количество элементов перед текущим
            link.nodes[0].num_before_me = link.nodes[0].num_before_me - 1

            if link.nodes[0].num_before_me == 0:
                ready.append(link.nodes[0])
    trigger = [node for node in ready if node.num_before_me == 0]
    if any(trigger):
        return None


def contains_cycle(node):
    """
    Определяет наличие цикла
    :param node: стартовый узел
    :return:
    """
    # пытаемся отсортировать сеть топологически
    if extend_partial_ordering(node) == None:
        return True
    return False


# цвета для закрашивания (считаю что RGB)
color1 = (0, 0, 0)
color2 = (255, 255, 255)

def two_color(node):
    """
    Алгоритм закрашивания двумя цветами
    :param node: стартовый узел
    :return:
    """
    # Создаем очередь для закрашенных узлов
    colored = Enqueue()

    # закрашиваю первый узел и добавляю его в список
    first_node = node.neighbors[0]
    first_node.Color = color1
    colored.push(first_node)

    # обходим сеть, закрашивая узлы
    while colored.values:
        # берем следующий узел из списка закрашенных
        node = colored.pop()

        # вычисляю цвет соседних узлов
        neighbor_color = color2 if node.Color == color1 else color1

        # Закрашиваем соседние узлы
        for link in node.links:
            neighbor = link.nodes[0]

            # смотрим, не закрашены ли соседние узлы - если да, то объект невозможно закрасить
            if neighbor.Color == node.Color:
                return
            # соседний узел уже был правильно закрашен, больше ничего не делаем
            elif neighbor.Color == neighbor_color:
                continue
            # соседний узел не был закрашен, закрашиваем
            else:
                neighbor.Color = neighbor_color
                colored.push(neighbor)

