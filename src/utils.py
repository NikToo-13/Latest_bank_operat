import json


def json_to_dictionary(path_file: str) -> dict:
    """которая принимает на вход путь до JSON-файла
        и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path_file, "r", encoding='utf-8') as file:
            date_files = json.load(file)
        return date_files
    except Exception:
        return []
