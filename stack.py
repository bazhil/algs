# coding=utf-8


class Stack:
    """
    Класс стека
    """

    def __init__(self):
        self.values = []
        self.next = 0


    def push(self, new_value):
        """
        Метод помещения элемента в стэк
        :param next: индекс следующего элемента
        :param new_value: новое значение
        :return:
        """
        self.values.append(new_value)
        self.next += 1


    def pop(self):
        """
        Метод извлечения элемента из стэка
        :return:
        """
        if self.next == 0:
            return
        self.next -= 1

        return self.values.pop(-1)


class DoubleStack(Stack):
    """
    Двойной стек, у которого добавление и извлечение данных идет с обоих сторон
    """
    def __init__(self):
        super().__init__()
        self.values = [None]
        self.before = 0

    def push_in_start(self, value):
        """
        Помещает элемент в начало стека
        :param value: переменная
        :return:
        """
        self.values.insert(0, value)
        self.before += 1


    def pop_from_start(self):
        """
        Извлекает элемент из начала списка
        :return:
        """
        if self.before == 0:
            return
        self.before -= 1

        return self.values.pop(0)


if __name__ == '__main__':
    # st = Stack()
    # for i in range(5):
    #     st.push(i)
    # for i in range(6):
    #     print(st.pop())

    ds = DoubleStack()
    for i in range(5):
        ds.push(i)
        ds.push_in_start(i+10)
    for i in range(6):
        print(ds.pop_from_start(), ds.pop())

