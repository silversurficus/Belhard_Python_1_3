"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Отредактировать функцию tip, которая принимает сумму из ресторанного чека так,
чтобы она возвращала чаевые (15% от суммы) и cashback (3% от суммы)

ПРИМЕРЫ
--------------------------------------------------------------------------------
- tip('150') -> 22.50, 4.50
- tip('632') -> 94.80, 18.96
"""


def tip(bill: str) -> tuple:
    """Рассчитывает чаевые и cashback в зависимости от переданного значения

    :param bill: сумма чека в ресторане
    :type bill: float

    :return: Кортеж, где первое значение - размер чаевых (15%),
        а второе значение - размер cashback (3%)
    :rtype: tuple
    """
    bill_to_float = float(bill)
    chayeviye = bill_to_float * 15 / 100
    cashback = bill_to_float * 3 / 100
    return chayeviye, cashback


if __name__ == '__main__':
    bill = input('Введите сумму из чека: ')
    result = tip(bill)
    print(f'Чаевые, cashback: {result[0]:.2f}, {result[1]:.2f}')
