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


    def get_var_names(self):
        """
        Метод получения имени списком строк
        :return:
        """
        return [k for k, v in globals().items() if v is self]


    def __str__(self):
        """
        Метод получения имени строкой
        :return:
        """
        result = self.get_var_names()
        return result[0] if result else 'UNDEFINED'


    def traverse_preorder(self, node):
        """
        Рекуурсивный обход вершин в прямом порядке
        :param node: узел дерева
        :return:
        """
        print(f'Обработка вершины дерева {self.__str__()}')
        if node.left_child:
            print(f'left_child is {node.left_child.__str__()}')
            self.traverse_preorder(node.left_child)
        if node.right_child:
            print(f'right_child is {node.right_child.__str__()}')
            self.traverse_preorder(node.right_child)



    def traverse_inorder(self, node):
        """
        Симметричный обход дерева
        :param node: узел дерева
        :return:
        """
        if node.left_child:
            print(f'value of left_child is {node.left_child.__str__()}')
            self.traverse_inorder(node.left_child)
        print(f'Обработка вершины дерева {self.__str__()}')
        if node.right_child:
            print(f'value of right_child is {node.right_child.__str__()}')
            self.traverse_inorder(node.right_child)


    def traverse_postoder(self, node):
        """
        Симметричный обход дерева
        :param node: узел дерева
        :return:
        """
        if node.left_child:
            print(f'value of left_child is {node.left_child.__str__()}')
            self.traverse_postoder(node.left_child)
        if node.right_child:
            print(f'value of right_child is {node.right_child.__str__()}')
            self.traverse_postoder(node.right_child)
        print(f'Обработка вершины дерева {self.__str__()}')


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
            print(f'Обработка вершины дерева {self.__str__()}')

            if node.left_child:
                print(f'value of left_child is {node.left_child.__str__()}')
                children.push(node.left_child)
            if node.right_child:
                print(f'value of right_child is {node.right_child.__str__()}')
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


    def add_node(self, new_value):
        """
        Добавление вершины к упорядоченному поддереву
        :return:
        """
        # сравниваю значение с уже имеющимся
        if new_value < self.value:
            # если новое значение меньше, добавляю его к левому поддереву
            if self.left_child:
                self.left_child.add_node(new_value)
            else:
                child = BinaryNode(new_value)
                self.left_child = child
                self.right_child = None

        # если значение не меньше - добавляю его к правому поддереву
        else:
            if self.right_child:
                self.right_child.add_node(new_value)
            else:
                child = BinaryNode(new_value)
                self.left_child = None
                self.right_child = child


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


class ExpressionNode:
    """
    Вершина дерева математического выражения
    """
    def __init__(self, operator, left_operand, right_operand, literal_text):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.literal_text = literal_text


    def evaluate(self):
        if self.operator == 'literal':
            return self.literal_text
        elif self.operator == 'plus':
            return self.left_operand.evaluate() + self.right_operand.evaluate()
        elif self.operator == 'minus':
            return self.left_operand.evaluate() - self.right_operand.evaluate()
        elif self.operator == 'times':
            return self.left_operand.evaluate() * self.right_operand()
        elif self.operator == 'divide':
            return self.left_operand.evaluate() / self.right_operand.evaluate()
        elif self.operator == 'negate':
            return - self.left_operand.evaluate()


class Rectangle:
    """
    Заглушка для создания квадрата
    """
    def __init__(self, left, top, wid, hgt):
        self.left = left
        self.top = top
        self.wid = wid
        self.hgt = hgt


class QuadtreeNode:
    """
    Класс узла дерева квадрантов (пока не понял, как проверять и отлаживать)
    Нужно подумать на каком-то примере, в учебнике не все понятно.
    """
    max_items = 10

    def __init__(self, area):
        self.max_items = 10
        self.area = area
        self.items = []
        self.Xmid = (self.area.left + self.area.right) / 2
        self.Ymid = (self.area.top + self.area.bottom) / 2
        self.NWChild = None
        self.NEChild = None
        self.SEChild = None
        self.SWChild = None


    def add_item(self, new_area):
        # проверяем, полная ли вершина
        if new_area.items and len(new_area.items) + 1 > new_area.max_items:
            # разбиваем вершину
            wid = (new_area.right + new_area.left) / 2
            hgt = (new_area.bottom + new_area.top) / 2
            NWChild = QuadtreeNode(Rectangle(new_area.left, new_area.top, wid, hgt))
            NEChild = QuadtreeNode(Rectangle(new_area.left + wid, new_area.top, wid, hgt))
            SEChild = QuadtreeNode(Rectangle(new_area.left + wid, new_area.top + hgt, wid, hgt))
            SWChild = QuadtreeNode(Rectangle(new_area.left, new_area.top + hgt, wid, hgt))

            # раскладываем точки в подходящее поддерево
            for item in new_area.items:
                if item.Y < self.Ymid:
                    if item.X < self.Xmid:
                        self.NWChild.add_item(item)
                    else:
                        self.NEChild.add_item(item)
                else:
                    if item.X < self.Xmid:
                        self.SWChild.add_item(item)
                    else:
                        self.SEChild.add_item(item)

            # удаляем вершины
            new_area.items = []

            # ? добавляем элемент в подходящее поддерево
            if self.items:
                self.items.append(item)
            elif new_area.Y < self.Ymid:
                if new_area.X < self.Xmid:
                    self.NWChild.add_item(new_area)
                else:
                    self.NEChild.add_item(new_area)
            else:
                if new_area.X < self.Xmid:
                    self.SWChild.add_item(new_area)
                else:
                    self.SEChild.add_item(new_area)


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

    root.add_node(10)

    # обходим дерево разными способами
    # root.traverse_preorder(root)
    # root.traverse_inorder(root)
    # root.traverse_postoder(root)
    # root.traverse_depth_first(root)
    # root.find_node(3)

    root.inorder_with_threads(root)