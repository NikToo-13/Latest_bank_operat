import csv
import os
import mock_open
from unittest.mock import patch, mock_open, Mock
import pandas as pd
import pytest

from project_sys import PATH_HOME
from src.read_csvexcel import read_csv, read_excels

PATCH_FILE_CSV = os.path.join(PATH_HOME, 'data', 'transactions_test.csv')


@patch('src.read_csvexcel.open', new_callable=mock_open, read_data='id,state,date\n441945886,EXECUTED,2019-08-26T10:50:58.294041\n')
def test_read_csv(mock_file):
    """функция тестирует верные данные"""
    result = read_csv('dir_transactions')
    assert result == [{'id,state,date': '441945886,EXECUTED,2019-08-26T10:50:58.294041'}]

def test_read_csv0():
    """функция тестирует неверный путь к файлу"""
    assert read_csv('') ==[]

#__________________________________________
@patch('src.read_csvexcel.pd.read_excel')
def test_read_excels(mock_read_excel, fix_data_exels):
    """Функция теста Exel файлов"""
    mock_read_excel.return_value = fix_data_exels
    assert read_excels('test.txt') == fix_data_exels.to_dict(orient='records')

def test_read_excels():
    """функция тестирует неверный путь к файлу"""
    assert read_excels('') == []
