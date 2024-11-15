def filter_by_state(list_dictionary: list, state_key: str = 'EXECUTED') -> list:
    """Функция возвращает новый список словарей, содержащий только те словари,
                       у которых ключ state соответствует указанному значению."""

    new_dictionary = []
    if state_key != '':
        for dictionary in list_dictionary:
            if dictionary['state'] == state_key:
                new_dictionary.append(dictionary)
        if new_dictionary == []:
            return 'Отсутствуют записи с данным статусом'
        else:
            return new_dictionary
    else:
        return 'Некоректный статус'



def sort_by_date(list_dictionary: list, sort_revers: bool = True) -> list:
    """Функция которая принимает список словарей и необязательный параметр,
            задающий порядок сортировки по дате False/True (по умолчанию — возростание(True))"""

    list_dictionary = sorted(list_dictionary, key=lambda list_dictionary: list_dictionary["date"], reverse=sort_revers)
    return list_dictionary
