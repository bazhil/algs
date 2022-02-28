#coding: utf-8
"""
Файл с алгоритмами на графах
"""
from sympy import S
from .stack import Stack


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
        self.visited = False


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


def get_connected_components(self, nodes: list):
    """
    Обход всех связанных элементов в сети
    :param nodes: список узлов
    :return: список связанных узлов
    """
    # количество посещенных узлов
    num_visited = 0

    # результат в виде списка списков
    components = []

    # инициализирую стек
    stack = Stack()

    # обходим, пока все узлы не попадут в связанный компонент
    while num_visited < len(nodes):
        # находим узел, который еще не посещали
        start_node = None
        for node in nodes:
            if not node.visited:
                start_node = node

        # добавляем начальный узел в стек
        stack.push(start_node)

        num_visited += 1

        # добавляем узел в новый связный компонент
        component = []
        component.append(start_node)
        components.append(component)

        # обрабатываем, пока стек не пустой
        while stack.values:
            # берем из стека следующий узел
            node = stack.pop()
            # обрабатываем звенья узла
            for link in node.links:
                # используем звено только если целевой узел еще не посещали
                if not link.nodes[0].visited:
                    link.nodes[0].visited = True

                    # помечаем звено, как часть дерева
                    link.visited = True
                    num_visited += 1

                    component.append(link.nodes[0])
                    stack.push(link.nodes[0])

    return components


def distance(start_node, end_node):
    """
    определяет расстояние между узлами
    :param start_node: начальный узел
    :param end_node: конечный узел
    :return:
    """
    # считаю, что у каждого узла есть координаты, по которым можно определить расстояние
    return abs(start_node.cooordinate - end_node.link.cooordinate)


def via(start_node, end_node):
    """
    Определяет промежуточный путь
    :param start_node: начальный узел
    :param end_node: конечный узел
    :return:
    """
    # если есть общие звенья - возвращаю их список
    elems = set(start_node.links.nodes).intersection(end_node.links.nodes)
    if len(elems) > 0:
        return list(elems)


def find_path(start_node, end_node):
    """
    Находит кратчайший путь от начального узла к целевому
    :param start_node: начальный узел
    :param end_node: конечный узел
    :return:
    """
    # проверяю, если ли путь, между данными узлами
    if distance(start_node, end_node) == S.Infinity:
        return None

    # получаем промежуточный узел для этого пути
    via_node = via(start_node, end_node)
    # если есть прямое соединение - возвращаю список, содержащий только конечный узел
    if via_node == end_node:
        return [end_node]
    # если прямого соединения нет
    else:
        return find_path(start_node, via_node) + find_path(via_node, end_node)
