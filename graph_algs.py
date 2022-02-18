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
