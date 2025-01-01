import os
from unittest.mock import mock_open, patch

from project_sys import PATH_HOME
from src.utils import json_to_dictionary, convert_date_to_general

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
    assert convert_date_to_general(fix_convert_date_to_general) == [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'operationAmount': {'amount': '16210', 'currency': {'name': 'Sol', 'code': 'PEN'}}, 'description': 'Перевод организации', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397'}]


# Тест на  пустой словарь.
def test_convert_date_to_general0():
    assert convert_date_to_general([]) == []

