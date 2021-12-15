# coding: utf-8
"""
Файл с алгоритмами бинарных деревьев
"""

class BinaryNode:
    """
    Узел бинарного дерева
    """

    def __init__(self, name):
        self.name = name
        self.left_child = None
        self.right_child = None


class TreeNode:
    """
    Класс вершины, допускающий любое количество дочерних элементов
    """

    def __init__(self, name):
        self.name = name
        # self.children = None
        # self.parent = None
        # self.child_data = []
        self.branches = None


class Branch:
    """
    Класс ветви дерева
    """

    def __init__(self, name):
        self.name = name
        self.branches = []


if __name__ == '__main__':
    # выстраиваю дерево
    root = BinaryNode("4")
    node1 = BinaryNode("1")
    node2 = BinaryNode("2")
    node3 = BinaryNode("3")
    node5 = BinaryNode("5")
    node6 = BinaryNode("6")
    node7 = BinaryNode("7")
    node8 = BinaryNode("8")

    root.left_child = node2
    root.right_child = node5
    node2.left_child = node1
    node2.right_child = node3
    node5.left_child = node6
    node5.right_child = node8
