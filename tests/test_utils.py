import json
import os

import pytest

from unittest.mock import Mock, patch, mock_open

from project_sys import PATH_HOME
from src.utils import json_to_dictionary

PATH_HOMES=os.path.join(PATH_HOME, 'data', 'operations.json')

# Тест проверки функций json_to_dictionary модуля utils.py.
# Если файл пустой, содержит не список или не найден, функция возвращает пустой список.


# json_to_dictionary проверка функции
# фикстура

def test_json_to_dictionary(fix_json_to_dictionary):
    assert str(type(json_to_dictionary(fix_json_to_dictionary))) == "<class 'list'>"

# неверный путь
def test_json_to_dictionary1(fix_json_to_dictionary1):
    assert json_to_dictionary(fix_json_to_dictionary1) == []

#тест для новых функции, используя Mock и patch.
# Тест на корректный файл с транзакциями
@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_json_to_dictionary2(mock_file):
    transactions = json_to_dictionary("data/operations.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]
    mock_file.assert_called_once_with('data/operations.json', 'r', encoding='utf-8')

# Тест на пустой файл
@patch("builtins.open", new_callable=mock_open, read_data='')
def test_empty_file(mock_file):
    transactions = json_to_dictionary("data/operations.json")
    assert transactions == []
    mock_file.assert_called_once_with('data/operations.json', 'r', encoding='utf-8')

# Тест на случай, если файл не найден
@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file):
    transactions = json_to_dictionary("data/operations.json")
    assert transactions == []
    mock_file.assert_called_once_with('data/operations.json', 'r', encoding='utf-8')
