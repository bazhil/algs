# coding=utf-8


class Enqueue:
    """
    Класс очередь. FIFO
    """
    def __init__(self):
        self.values = []


    def push(self, value):
        """
        Добавление элемента в очередь
        :param value: переменная
        :return:
        """
        self.values.append(value)


    def pop(self):
        """
        Извлечение первого элемента из очереди
        :return:
        """
        return self.values.pop(0) if len(self.values) else None


class Deka(Enqueue):
    """
    Очередь с двухсторонним доступом
    """
    def __init__(self):
        super(Deka, self).__init__()


    def push_in(self, value):
        """
        Помещает элемент в начало очереди
        :param value:
        :return:
        """
        self.values.insert(0, value)


    def end_pop(self):
        """
        Достает элемент из конца очереди
        :return:
        """
        return self.values.pop(len(self.values) - 1) if len(self.values) else None



if __name__ == '__main__':
    enq = Enqueue()
    dek = Deka()

    for i in range(6):
        enq.push(i)
        dek.push_in(i)
        dek.push(i*3 + 1)

    for i in range(10):
        # print(enq.pop())
        print(dek.pop(), dek.end_pop())