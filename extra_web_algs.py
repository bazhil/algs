# coding: utf-8

from .graph_algs import GraphNode

# инициализирую граф
node = GraphNode()

# список упорядоченных узлов
ordered_nodes = []

def extend_partial_ordering(node):
    """
    Упорядочивает узлы
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
