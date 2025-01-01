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
        legend_s = " Функция: json_to_dictionary -> "
        logger.info(f"{legend_s}Принимаем путь к файлу: {path_file}")
        with open(path_file, "r", encoding="utf-8") as file:
            date_file = json.load(file)
        logger.info(f"{legend_s}{path_file} - прочтен успешно")
        return date_file
    except Exception as er:
        logger.error(f"{legend_s}Ошибка: {er}")
        return []

def convert_date_to_general(dicts: list) ->list:
    """Функция приводит формат данных с файлов типа EXEL и CSV  к формату полученому из JSON файла."""

    try:
        legend_s = f' Функция: convert_date_to_general -> '
        list_transaction = []
        logger.info(f"{legend_s}преабразуем файл под наши функции")
        for row in dicts:
            dict_transaction = {
                "id": str(row["id"]),
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": str(row["amount"]),
                    "currency": {
                        "name": row["currency_name"],
                        "code": row["currency_code"]
                    }
                },
                "description": row["description"],
                "from": row["from"],
                "to": row["to"]
            }
            list_transaction.append(dict_transaction)
        logger.info(f"{legend_s}Работа со списком успешно завершена!")
        return list_transaction
    except Exception as er:
        logger.error(f"{legend_s}Ошибка: {er}")
        return []
