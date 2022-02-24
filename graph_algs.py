#coding: utf-8
"""
Файл с алгоритмами на графах
"""


class GraphNode:
    """
    Вершина графа
    """
    def __init__(self, name, neighbors, costs):
        """
        инициализация параметром
        :param name: название вершины
        :param neighbors: соседи
        :param costs: цены
        """
        self.name = name
        self.neighbors = neighbors
        self.costs = costs
        self.links = []


class Node:
    """
    Вершина ненаправленного графа
    """
    def __init__(self, name, links):
        """
        Инициализация параметров
        :param name: название вершины
        :param links: список ссылок на соседей
        """
        self.name = name
        self.links = links
        # переменная, которая отмечает
        self.visited = True


    def traverse(self):
        """
        Обход в глубину
        :return:
        """
        # помечаю узел, чтобы повторно не обходить
        self.node.visited = True
        # TODO: обработать текущий узел
        for link in self.links:
            if not link.nodes[1].visited:
                link.nodes.traverse()


    def depth_first_traverse(self, start_node):
        """
        Обход в глубину с использованием стека
        :param start_node: стартовый узел
        :return:
        """
        # посещаем узел
        start_node.visiterd = True

        # создаем стек и помещаем в него начальный узел
        stack = []
        stack.append(start_node)

        # повторяем, пока стек не станет пустым
        while len(stack) > 0:
            node = stack.pop()
            for link in node.links:
                # используем узел только если он не посешался и отмечаем
                if not link.nodes[0].visited:
                    # действия над узлом
                    link.nodes[0].visited = True
                    stack.append(link.nodes[0])


    def is_connected(self, start_node):
        """
        Алгоритм проверки связности
        :param start_node: стартовый узел
        :return:
        """
        # обходим сеть, начиная со start_node
        self.traverse()

        # смотрим, не остался ли какой-то узел не посещенным
        for link in start_node.links:
            if not link.nodes[0].visited:
                return False

        return True


class Link:
    """
    Связь в ненаправленном графе
    """
    def __init__(self, cost, nodes):
        """
        инициализация параметром
        :param cost: цена связи
        :param nodes: список с двумя вершинами
        """
        self.cost = cost
        self.nodes = nodes


class OrderedNode:
    """
    Вершина упорядоченного графа
    """
    def __init__(self, name):
        """
        Инициализация параметров
        :param name: имя вершины
        """
        self.name = name
        self.links = []


class OrderedLink:
    """
    Связь упорядоченного графа
    """
    def __init__(self, cost, to_node):
        """
        Инициализация параметров
        :param cost: цена
        :param to_node: к какой вершине направлена связь
        """
        self.cost = cost
        self.to_node = to_node
