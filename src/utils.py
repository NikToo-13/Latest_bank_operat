import json
import logging

from project_sys import PATH_HOME

path_ = f"{PATH_HOME}/logs/utils.log"
logger = logging.getLogger("utils")
file_handler = logging.FileHandler(path_, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def json_to_dictionary(path_file: str) -> dict:
    """которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        logger.info(f"Принимаем путь к файлу: {path_file}")
        with open(path_file, "r", encoding="utf-8") as file:
            date_file = json.load(file)
        logger.info(f"{path_file} - прочтен успешно")
        return date_file
    except Exception as er:
        logger.error(f"Ошибка: {er}")
        return []
