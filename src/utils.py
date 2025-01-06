import json
import logging
import re
from collections import Counter

from project_sys import PATH_HOME

path_ = f"{PATH_HOME}/logs/utils.log"
logger = logging.getLogger("utils")
file_handler = logging.FileHandler(path_, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def json_to_dictionary(path_file: str) -> list:
    """которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        legend_s = " Функция: json_to_dictionary -> "
        logger.info(f"{legend_s}Принимаем путь к файлу: {path_file}")
        with open(path_file, "r", encoding="utf-8") as file:
            date_file = json.load(file)
        logger.info(f"{legend_s}{path_file} - прочтен успешно")
        return date_file
    except Exception as er:
        logger.error(f"{legend_s}Ошибка: {er}")
        return []


def convert_date_to_general(dicts: list) -> list:
    """Функция приводит формат данных
    с файлов типа EXEL и CSV  к формату полученому из JSON файла.
      В случии ошибки возвращает пустой список"""

    try:
        legend_s = " Функция: convert_date_to_general -> "
        list_transaction = []
        logger.info(f"{legend_s}преабразуем файл под формат работы внутренних функций")
        for row in dicts:
            dict_transaction = {
                "id": str(row["id"]),
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": str(row["amount"]),
                    "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                },
                "description": row["description"],
                "from": row["from"],
                "to": row["to"],
            }
            list_transaction.append(dict_transaction)
        logger.info(f"{legend_s}Работа со списком успешно завершена!")
        return list_transaction
    except Exception as er:
        logger.error(f"{legend_s}Ошибка: {er}")
        return []


def transaction_search(list_dict: list, searchs: str) -> list:
    """Функция принимать список словарей с данными и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка."""

    try:
        legend_s = " Функция: transaction_search -> "
        list_search = []
        logger.info(f"{legend_s}Начинаем фильтрацию по запросу пользователя в описании транзакций.")
        if searchs != "":
            for list_s in list_dict:
                if re.findall(searchs, str(list_s["description"]), re.I):
                    list_search.append(list_s)
            if list_search != []:
                logger.info(f'{legend_s}Найдены совпадения пользовательского запроса: "{searchs}"')
                return list_search
            else:
                logger.info(f'{legend_s}Нет совпадения пользовательского запроса: "{searchs}"')
                return []
        else:
            logger.warning(f"{legend_s}Пустой запрос!!!")
            return []
    except Exception as er:
        logger.error(f"{legend_s}Ошибка: {er}")
        return []


def counting_transactions_category(list_transactions: list, listof_categories: list) -> dict:
    """Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь: ключ — это названия категорий, а значения — это количество операций в каждой категории"""

    try:
        legend_s = " Функция: counting_transactions_category -> "
        logger.info(f"{legend_s}Начинаем подсчет операций в каждой категории.")
        lists_search = []
        for lines in list_transactions:
            if lines["description"] in listof_categories:
                lists_search.append(lines["description"])
        categories_counter = Counter(lists_search)
        logger.info(f"{legend_s}Подсчет успешно закончен.")
        return categories_counter
    except Exception as er:
        logger.error(f"{legend_s}Ошибка: {er}")
        return {}
