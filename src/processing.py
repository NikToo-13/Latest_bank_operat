from typing import Any


def filter_by_state(list_dictionary: list, state_key: str = "EXECUTED") -> Any:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    new_dictionary = []
    if state_key != "":
        for dictionary in list_dictionary:
            if dictionary["state"] == state_key:
                new_dictionary.append(dictionary)
        if new_dictionary == []:
            return "Отсутствуют записи с данным статусом"
        else:
            return new_dictionary
    else:
        return "Некоректный статус"


def sort_by_date(list_dictionary: list, sort_revers: bool = True) -> Any:
    """Функция которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки по дате False/True (по умолчанию — возростание(True))"""
    try:
        # проверка на некоректность формата даты
        if list_dictionary != []:
            for list_entry in list_dictionary:
                is_data = list_entry["date"]
                if not (
                    is_data[:4].isdigit()
                    and is_data[4] == "-"
                    and is_data[7] == "-"
                    and is_data[5:7].isdigit()
                    and is_data[8:10].isdigit()
                ):
                    return "Некоректные данные"
                if not (0 < int(is_data[5:7]) < 13 and 0 < int(is_data[8:10]) < 32):
                    return "Некоректные данные"
            list_dictionary = sorted(
                list_dictionary, key=lambda list_dictionary: list_dictionary["date"], reverse=sort_revers
            )
        else:
            return "Некоректные данные"
    except Exception:
        return "Некоректные данные"
    return list_dictionary
