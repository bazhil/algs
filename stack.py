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

        return self.values[self.next]


if __name__ == '__main__':
    st = Stack()
    for i in range(5):
        st.push(i)
    for i in range(6):
        print(st.pop())
