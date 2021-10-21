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


def hanoi_tower(first_tower: Stack, second_tower: Stack, third_tower: Stack) -> Stack:
    """
    Реализация решения задачи Ханойская башня
    Выполняется за (2**N - 1) шагов
    :param first_tower: первая башня (стек)
    :param second_tower: вторая башня (стек)
    :param third_tower: третья башня (стек)
    :return:
    """
    second_tower.push(first_tower.pop())
    third_tower.push(first_tower.pop())
    third_tower.push(second_tower.pop())
    second_tower.push(first_tower.pop())
    first_tower.push(third_tower.pop())
    second_tower.push(third_tower.pop())
    second_tower.push(first_tower.pop())

    return second_tower


def insertion_sort(items: list) -> list:
    """
    Сортировка вставкой
    :param items: неотсортированный стек
    :return:
    """
    for i in range(1, len(items)):
        next_item = items[i]
        j = i - 1
        while j >= 0 and next_item < items[j]:
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = next_item

    return items


def selection_sort(items):
    """
    Сортировка выбором
    :param items:
    :return:
    """
    for i in range(len(items)):
        min = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min]:
                min = j

        items[min], items[i] = items[i], items[min]

    return items


if __name__ == '__main__':
    # TODO: оформить примеры в тесты с использованием библиотек/фреймворков
    # st = Stack()
    # for i in range(5):
    #     st.push(i)
    # for i in range(6):
    #     print(st.pop())

    # ds = DoubleStack()
    # for i in range(5):
    #     ds.push(i)
    #     ds.push_in_start(i+10)
    # for i in range(6):
    #     print(ds.pop_from_start(), ds.pop())

    # first, second, third = Stack(), Stack(), Stack()
    # for i in [3, 2, 1]:
    #     first.push(i)
    #
    # second = hanoi_tower(first, second, third)
    # for i in range(4):
    #     print(second.pop())

    # st = Stack()
    test_data = [9, 2, 6, 10, 3, 1]
    # for i in test_data:
    #     st.push(i)
    # print(f'Test data: {test_data}')
    # sorted_data = insertion_sort(test_data)
    # print(f'Sorted data: {sorted_data}')

    print(f'Test data: {test_data}')
    sorted_data = selection_sort(test_data)
    print(f'Sorted data: {sorted_data}')



