import os

import pandas as pd
import pytest

from project_sys import PATH_HOME


@pytest.fixture
def fix_get_mask_card_number():
    """Фикстуры для test_masks.py"""
    return "7000792289606361"


@pytest.fixture
def fix_get_mask_account():
    return "73654108430135874305"


@pytest.fixture
def fix_mask_account_card():
    """Фикстуры для test_widget.py"""
    return "Maestro 1596837868705199"


@pytest.fixture
def fix_mask_account_card_c():
    """Фикстуры для test_widget.py"""
    return "Счет 35383033474447895560"


@pytest.fixture
def fix_get_date():
    """Фикстуры для test_widget.py"""
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def fix_filter_by_state():
    """Фикстуры для test_processing.py"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def fix_sort_by_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def fix_sort_by_date0():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064531, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064541, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064551, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def fix_sort_by_date_n():
    return "Некоректные данные"


@pytest.fixture
def fix_data_test_list():
    return ""


@pytest.fixture
def fix_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def fix_json_to_dictionary():
    """Общая работа (когда верное значение на выходе)"""
    return os.path.join(PATH_HOME, "data", "operations.json")


@pytest.fixture
def fix_json_to_dictionary1():
    """Фикстуры для test_utils.py неверный путь"""
    return os.path.join(PATH_HOME, "data", "operations_0.json")


@pytest.fixture
def exit_answer():
    return {"id,state,date": "441945886,EXECUTED,2019-08-26T10:50:58.294041"}


@pytest.fixture
def fix_data_exels():
    """Фикстура для подмены Exel данных файла"""
    path_file = os.path.join(PATH_HOME, "data", "transactions_excel_test.xlsx")
    return pd.read_excel(path_file)
