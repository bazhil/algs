# coding=utf-8
"""
Файл с алгоритмами использующими рекурсию
"""
import turtle

t = turtle.Turtle()


def draw_koch_segment(t, ln):
    if ln > 6:
        ln3 = ln // 3
        draw_koch_segment(t, ln3)
        t.left(60)
        draw_koch_segment(t, ln3)
        t.right(120)
        draw_koch_segment(t, ln3)
        t.left(60)
        draw_koch_segment(t, ln3)
    else:
        t.fd(ln)
        t.left(60)
        t.fd(ln)
        t.right(120)
        t.fd(ln)
        t.left(60)
        t.fd(ln)


def hilbert(level, angle, step):
    """
    Метод рисующий кривую Гильберта
    :param level: глубина кривой
    :param angle: угол поворота
    :param step: шаг
    :return:
    """
    if level == 0:
        return

    t.right(angle)
    hilbert(level - 1, -angle, step)

    t.forward(step)
    t.left(angle)
    hilbert(level - 1, angle, step)

    t.forward(step)
    hilbert(level - 1, angle, step)

    t.left(angle)
    t.forward(step)
    hilbert(level - 1, -angle, step)
    t.right(angle)


def sierpinski(length, depth):
    if depth == 0:
        for i in range(0, 3):
            t.fd(length)
            t.left(120)
    else:
        sierpinski(length//2, depth-1)
        t.fd(length//2)
        sierpinski(length//2, depth-1)
        t.bk(length//2)
        t.left(60)
        t.fd(length//2)
        t.right(60)
        sierpinski(length // 2, depth - 1)


if __name__ == '__main__':
    # draw_koch_segment(t, 20000)
    # hilbert(12, 90, 20)
    sierpinski(10, 20)