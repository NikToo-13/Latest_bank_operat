def filter_by_state(list_dictionary: list, state_key: str = 'EXECUTED') -> list:
    """Функция возвращает новый список словарей, содержащий только те словари,
                       у которых ключ state соответствует указанному значению."""

    new_dictionary = []
    for dictionary in list_dictionary:
        if dictionary['state'] == state_key:
            new_dictionary.append(dictionary)
    return new_dictionary


def sort_by_date(list_dictionary: list, sort_revers: bool = False) -> list:
    """Функция которая принимает список словарей и необязательный параметр,
            задающий порядок сортировки по дате False/True (по умолчанию — убывание(False))"""

    list_dictionary = sorted(list_dictionary, key=lambda list_dictionary: list_dictionary["date"], reverse=sort_revers)
    return list_dictionary
