# coding: utf-8
"""
Файл с алгоритмами бинарных деревьев
"""
from enqueue import Enqueue


class BinaryNode:
    """
    Узел бинарного дерева
    """

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


    def traverse_preorder(self, node):
        """
        Рекуурсивный обход вершин в прямом порядке
        :param node: узел дерева
        :return:
        """
        print(f'Обработка вершины дерева {node.value}')
        if node.left_child:
            print(f'value of left_child is {node.left_child.value}')
            self.traverse_preorder(node.left_child)
        if node.right_child:
            print(f'value of right_child is {node.right_child.value}')
            self.traverse_preorder(node.right_child)



    def traverse_inorder(self, node):
        """
        Симметричный обход дерева
        :param node: узел дерева
        :return:
        """
        if node.left_child:
            print(f'value of left_child is {node.left_child.value}')
            self.traverse_inorder(node.left_child)
        print(f'Обработка вершины дерева {node.value}')
        if node.right_child:
            print(f'value of right_child is {node.right_child.value}')
            self.traverse_inorder(node.right_child)


    def traverse_postoder(self, node):
        """
        Симметричный обход дерева
        :param node: узел дерева
        :return:
        """
        if node.left_child:
            print(f'value of left_child is {node.left_child.value}')
            self.traverse_postoder(node.left_child)
        if node.right_child:
            print(f'value of right_child is {node.right_child.value}')
            self.traverse_postoder(node.right_child)
        print(f'Обработка вершины дерева {node.value}')


    def traverse_depth_first(self, root):
        """
        Обход в ширину
        :param root: корень дерева
        :return:
        """
        # создаю очередь для хранения дочерних вершин
        children = Enqueue()

        # помещаю корень в очередь
        children.push(root)

        while children.values:
            # получаю следующую вершину в очереди
            node = children.pop()
            print(f'Обработка вершины дерева {node.value}')

            if node.left_child:
                print(f'value of left_child is {node.left_child.value}')
                children.push(node.left_child)
            if node.right_child:
                print(f'value of right_child is {node.right_child.value}')
                children.push(node.right_child)


    def find_node(self, target):
        """
        Метод поиска конкретной вершины по значению
        :param target: значение для поиска вершины
        :return:
        """
        # если нашли целевое значение, возвращаем вершину
        if target == self.value:
            print(f'Значение {target} найдено в узле {self.__str__()}')
            return self.value
        # смотрим, где целевое значение, в левом или правом поддереве
        if target < self.value:
            return None if not self.left_child else self.left_child.find_node(target)
        else:
            return None if not self.right_child else self.right_child.find_node(target)

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
    # создаю дерево
    root = BinaryNode(4)
    node1 = BinaryNode(1)
    node2 = BinaryNode(2)
    node3 = BinaryNode(3)
    node5 = BinaryNode(5)
    node6 = BinaryNode(6)
    node7 = BinaryNode(7)
    node8 = BinaryNode(8)

    root.left_child = node2
    root.right_child = node5
    node2.left_child = node1
    node2.right_child = node3
    node5.left_child = node6
    node5.right_child = node8


    # обходим дерево разными способами
    # root.traverse_preorder(root)
    # root.traverse_inorder(root)
    # root.traverse_postoder(root)
    # root.traverse_depth_first(root)
    root.find_node(8)