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
        list_transaction = []
        logger.info(f"Принимаем путь к файлу: {path_file}")
        with open(path_file, "r", encoding="utf-8") as st_file:
            date_file = csv.DictReader(st_file, delimiter=";")
            logger.info(f"Читаем файл: {path_file}")
            for row in date_file:
                list_transaction.append(row)
        return list_transaction
    except Exception as er:
        logger.error(f"Ошибка: {er}")
        return []


def read_excel(path_file: str) -> dict:
    """которая принимает на вход путь до Excel-файла
        и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        list_transaction = []
        logger.info(f"Принимаем путь к файлу: {path_file}")
        date_file = pd.read_excel(path_file, index_col=0)
        logger.info(f"Читаем файл: {path_file}")
        for row in date_file:
            list_transaction.append(row)
        return list_transaction
    except Exception as er:
        logger.error(f"Ошибка: {er}")
        return []