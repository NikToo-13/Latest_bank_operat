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

    def data_to_dictionary(date_files: list) -> dict:
        """Функция принимает список словорей и преобразует под нужный нам формат"""
        list_transaction = []
        #try:
        for row in date_files:
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
        logger.info(f"{legend_s}(data_to_dictionary) успешное преоброзование файла")
        return list_transaction
        #except Exception as er:
        #    logger.error(f"{legend_s}(data_to_dictionary) Ошибка преоброзование файла: {er}")
        #    return []


    def file_writes(path_files: str, delimiters: str =',') -> list:
        """Функция принимает путь к файлу и возвращает файл в виде листа словарей"""
        try:
            logger.info(f"{legend_s}(file_writes) Принимаем путь к файлу: {path_files}")
            with (open(path_files, "r", encoding="utf-8") as st_file):
                logger.info(f"{legend_s}(file_writes) Читаем файл: {path_files}")
                date_file = csv.DictReader(st_file, delimiter=delimiters)
                logger.info(f"{legend_s}(file_writes) преабразуем файл под наши функции")
                list_transaction = data_to_dictionary(date_file)
            return list_transaction
        except FileNotFoundError as er:
            logger.error(f"{legend_s}(file_writes) Ошибка: {er}")
            return []
        except:
            raise ValueError('Неверный разделитель')

    legend_s = f' Функция: read_csv -> '
    try:
        logger.info(f'{legend_s}- Обработка файла с разделителем ","')
        list_transactions = file_writes(path_file)
        return list_transactions
    except Exception as er:
        logger.warning(f'{legend_s}- Обработка файла с разделителем "," - некоректна ({er})')
        logger.info(f'{legend_s}- Обработка файла с разделителем ";"')
        list_transactions0 = file_writes(path_file, ';')
        return list_transactions0
    except FileNotFoundError as er:
        logger.error(f"{legend_s}Ошибка: {er}")
        return []
    except ValueError as er:
        logger.error(f"{legend_s}Ошибка: {er}")
        return []
    else:
        logger.critical(f"{legend_s}Ошибка!!!")
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
