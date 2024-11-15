from src.masks import get_mask_card_number, get_mask_account

import pytest


#Тест проверки функций get_mask_card_number и get_mask_account модуля masks.py при условии:
# что входящий параметр не может быть не числовым(начальное условие задания)

@pytest.mark.parametrize('value, expected', [
    ('7000792289606361', '7000 79** **** 6361'),
    ('7020652245672183', '7020 65** **** 2183'),
    ('700079228960636341','Проверти, правильность ввода номера карты!'),
    ('70008960636341','Проверти, правильность ввода номера карты!'),
    ('','Проверти, правильность ввода номера карты!')
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected

@pytest.mark.parametrize('value, expected', [
    ('73654108430135874305', '**4305'),
    ('73654107430195874235', '**4235'),
    ('736541084','Проверти, правильность ввода счета!'),
    ('73654107430195874235322','Проверти, правильность ввода счета!'),
    ('','Проверти, правильность ввода счета!')
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected