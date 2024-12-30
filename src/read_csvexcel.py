import csv
import logging
from typing import Any

import pandas as pd

from project_sys import PATH_HOME

path_ = f"{PATH_HOME}/logs/read_csvexcel.log"
logger = logging.getLogger("read_csvexcel")
file_handler = logging.FileHandler(path_, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_csv(path_file: str, delimiters: str = ";") -> list:
    """которая принимает на вход путь до csv-файла
    и возвращает список словарей с данными о финансовых транзакциях."""

    legend_s = " Функция: read_csv -> "
    try:
        with open(path_file, "r", encoding="utf-8") as st_file:
            logger.info(f"{legend_s}Читаем файл: {path_file}")
            date_file = csv.DictReader(st_file, delimiter=delimiters)
            logger.info(f"{legend_s}преабразуем файл в словарь")
            return list(date_file)
    except FileNotFoundError as eror:
        logger.error(f"{legend_s}Ошибка: {eror}")
        return []
    except ValueError as eror:
        logger.error(f"{legend_s}Ошибка: {eror}")
        return []
    else:
        eror = Exception
        logger.critical(f"{legend_s}Критическая ошибка: {eror}")
        return []


def read_excels(path_file: str) -> list[dict[Any, Any]] | list[Any]:
    """которая принимает на вход путь до Excel-файла
    и возвращает список словарей с данными о финансовых транзакциях."""

    try:
        legend_s = " Функция: read_excels -> "
        logger.info(f"{legend_s}Принимаем путь к файлу: {path_file}")
        date_freme = pd.read_excel(path_file)
        date_files = date_freme.to_dict("records")
        logger.info(f"{legend_s}Читаем файл: {path_file}")
        return date_files

    except FileNotFoundError as eror:
        logger.error(f"{legend_s}Ошибка: {eror}")
        return []
    except ValueError as eror:
        logger.error(f"{legend_s}Ошибка: {eror}")
        return []
    else:
        eror = Exception
        logger.critical(f"{legend_s}Критическая ошибка: {eror}")
        return []
