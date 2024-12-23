import csv
import logging

import pandas as pd

from project_sys import PATH_HOME

path_ = f"{PATH_HOME}/logs/read_csvexcel.log"
logger = logging.getLogger("read_csvexcel")
file_handler = logging.FileHandler(path_, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_csv(path_file: str) -> dict:
    """которая принимает на вход путь до csv-файла
        и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        legend_s = f' Функция: read_csv -> '
        list_transaction = []
        logger.info(f"{legend_s}Принимаем путь к файлу: {path_file}")
        with (open(path_file, "r", encoding="utf-8") as st_file):
            logger.info(f"{legend_s}Читаем файл: {path_file}")
            date_file = csv.DictReader(st_file, delimiter=";")
            for row in date_file:
                dict_transaction = {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": row["amount"],
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
        logger.info(f"{legend_s}преабразуем файл под наши функции")
        return list_transaction

    except Exception as er:
        logger.error(f"{legend_s}Ошибка: {er}")
        return []


def read_excels(path_file: str, excel_data_with_index=None) -> dict:
    """которая принимает на вход путь до Excel-файла
        и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        legend_s = f' Функция: read_excels -> '
        list_transaction = []
        logger.info(f"{legend_s}Принимаем путь к файлу: {path_file}")
        date_files = pd.read_excel(path_file)
        logger.info(f"{legend_s}Читаем файл: {path_file}")
        len_s, n_ = date_files.shape
        for index_ in range(0, len_s):
            dict_transaction = {
                "id": str(date_files["id"][index_])[:-2],
                "state": date_files["state"][index_],
                "date": date_files["date"][index_],
                "operationAmount": {
                    "amount": str(date_files["amount"][index_]),
                    "currency": {
                        "name": date_files["currency_name"][index_],
                        "code": date_files["currency_code"][index_]
                    }
                },
                "description": date_files["description"][index_],
                "from": date_files["from"][index_],
                "to": date_files["to"][index_]
                }
            list_transaction.append(dict_transaction)
        logger.info(f"{legend_s}преабразуем файл под наши функции")
        return list_transaction

    except Exception as er:
        logger.error(f"{legend_s}Ошибка: {er}")
        return []
