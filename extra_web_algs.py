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
