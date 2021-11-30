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



if __name__ == '__main__':
    # draw_koch_segment(t, 20000)
    hilbert(12, 90, 20)