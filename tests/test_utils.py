import os
from collections import Counter
from unittest.mock import mock_open, patch

import pytest

from project_sys import PATH_HOME
from src.utils import convert_date_to_general, counting_transactions_category, json_to_dictionary, transaction_search

PATH_HOMES = os.path.join(PATH_HOME, "data", "operations.json")

# Тест проверки функций json_to_dictionary модуля utils.py.
# Если файл пустой, содержит не список или не найден, функция возвращает пустой список.


# json_to_dictionary проверка функции
# фикстура
def test_json_to_dictionary(fix_json_to_dictionary):
    assert str(type(json_to_dictionary(fix_json_to_dictionary))) == "<class 'list'>"


# неверный путь
def test_json_to_dictionary1(fix_json_to_dictionary1):
    assert json_to_dictionary(fix_json_to_dictionary1) == []


# тест для новых функции, используя Mock и patch.
# Тест на корректный файл с транзакциями
@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_json_to_dictionary2(mock_file):
    transactions = json_to_dictionary("data/operations.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


# Тест на пустой файл
@patch("builtins.open", new_callable=mock_open, read_data="")
def test_empty_file(mock_file):
    transactions = json_to_dictionary("data/operations.json")
    assert transactions == []
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


# Тест на случай, если файл не найден
@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file):
    transactions = json_to_dictionary("data/operations.json")
    assert transactions == []
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


# Тест нормальной работы функции.
def test_convert_date_to_general(fix_convert_date_to_general):
    assert convert_date_to_general(fix_convert_date_to_general) == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        }
    ]


# Тест на  пустой словарь.
def test_convert_date_to_general0():
    assert convert_date_to_general([]) == []


# Тест на на нормальную работу и отсутствие данных
data_list = {
    "Перевод с карты на карту",
    "Перевод со счета на счет",
    "Открытие вклада",
    "Перевод организации",
}  # Список тестирование на категории


# параметризация
@pytest.mark.parametrize(
    "value, expected",
    [
        (
            data_list,
            {"Перевод организации": 2, "Перевод со счета на счет": 2, "Перевод с карты на карту": 1},
        ),
        ([], {}),
    ],
)
def test_counting_transactions_category_p(fix_transactions, value, expected):
    assert counting_transactions_category(fix_transactions, value) == expected


# Тест на пустой словарь транзакция
def test_counting_transactions_category(fix_transactions):
    assert counting_transactions_category([], data_list) == Counter()


# Тест на словарь транзакциq с неверной структурой
def test_counting_transactions_category0():
    assert counting_transactions_category([], data_list) == Counter()


# Тестирование функции convert_date_to_general на входные данные
# (верные, неправельная структура, ошибка ключа, пустое значение)
data_x0 = []
data_x1 = []
data_x2 = []
data_x0.append(
    {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
)
data_x1.append(
    {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
)
data_x2.append(
    {
        "id": "650703",
        "state": "EXECUTED",
        "dXate": "2023-09-05T11:30:32Z",
        "amouXnt": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "frXom": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
)


# параметризация
@pytest.mark.parametrize(
    "value, expected",
    [
        (
            data_x0,
            [
                {
                    "id": "650703",
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
                    "description": "Перевод организации",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                }
            ],
        ),
        (data_x1, []),
        (data_x2, []),
        ({}, []),
    ],
)
def test_convert_date_to_general2(value, expected):
    assert convert_date_to_general(value) == expected


# Тестирование функции transaction_search


@pytest.mark.parametrize(
    "value, expected",
    [
        ("", []),
        ("открытие", []),
        (
            "карту",
            [
                {
                    "date": "2018-08-19T04:27:37.904916",
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "id": 895315941,
                    "operationAmount": {"amount": "56883.54", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Visa Platinum 8990922113665229",
                }
            ],
        ),
    ],
)
def test_transaction_search(fix_transactions, value, expected):
    assert transaction_search(fix_transactions, value) == expected


# Пустой список словарей
def test_transaction_search0():
    assert transaction_search([], "открытие") == []
