def filter_by_state(list_dictionary: list, state_key = 'EXECUTED') -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению."""

    new_dictionary = []
    for dictionary in list_dictionary:
        if dictionary['state'] == state_key:
            new_dictionary.append(dictionary)
    return new_dictionary