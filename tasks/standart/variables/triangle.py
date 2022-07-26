"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Функция triangle получает длины 2х катетов прямоугольного треугольника.
Нужно отредактировать функцию таким образом,
чтобы она возвращала периметр, площадь и гипотенузу

ПРИМЕРЫ
--------------------------------------------------------------------------------
triangle(3, 4) -> (5, 12, 6)
"""
from math import sqrt

def triangle(side_1: int, side_2: int) -> tuple:
    """
    Рассчитывает гипотенузу, периметр и площадь

    :param side_1: первый катет
    :type side_1: int

    :param side_2: второй катет
    :type side_2: int

    :return: кортеж с параметрами
    :rtype: tuple
    """
    int_side_1 = int(side_1)
    int_side_2 = int(side_2)
    hypotenuse = sqrt(int_side_1**2+int_side_2**2)
    perimetr = int_side_1 + int_side_2 + hypotenuse
    ploshad = int_side_1 * int_side_2 / 2
    return hypotenuse, perimetr, ploshad


if __name__ == '__main__':
    side_1 = int(input('Введите длину первого катета: '))
    side_2 = int(input('Введите длину второго катета: '))
    print(f'(Гипотенуза, Периметр, Площадь): {triangle(side_1, side_2)}')
