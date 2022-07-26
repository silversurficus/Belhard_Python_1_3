"""
Написать функцию hide_debit_numbers которая скрывает номер платежной карты,
оставляя только первые 4 и последние 4 цифра, а остальные заменяет символом *

Пример:
1111222233334444 -> 1111********4444
"""


def hide_debit_numbers(card_number: str) -> str:
    """Скрывает номер карты, оставляя толdько первые и последние 4 цифры

    :param card_number: номер карты 16 цифр
    :return: номер карты, вида 1111********1111
    """
    noviy_nomer = card_number.replace(card_number[4:12], '********')
    return noviy_nomer


if __name__ == '__main__':
    card_number = input("Введите номер карты 16 цифр: ")
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Некорректный номер карты")
    print(hide_debit_numbers(card_number))
