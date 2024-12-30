import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

date_transactions = [
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


# filter_by_currency - проверка функции что корректно фильтрует транзакции
# по заданной валюте.
# Тест генератора
def test_filter_by_currency(fix_transactions):
    generator = filter_by_currency(fix_transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


# Параметаризация
@pytest.mark.parametrize(
    "value, expected",
    [
        (
            "USD",
            [
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
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
        )
    ],
)
def test_filter_by_currency_p(value, expected):
    assert list(filter_by_currency(date_transactions, value)) == expected


def test_filter_by_currency1(fix_transactions):
    generator = filter_by_currency(fix_transactions, "RUB")
    assert next(generator) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(generator) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


def test_filter_by_currency2(fix_transactions):
    try:
        generator = filter_by_currency(fix_transactions, "YAN")
        assert next(generator) == "Список словарей закончился"
    except StopIteration:
        print("StopIteration")


# Пустой список словарей
def test_filter_by_currency3(fix_transactions):
    try:
        generator = filter_by_currency([], "USD")
        assert next(generator) == "Список словарей закончился"
    except StopIteration:
        print("StopIteration")


# transaction_descriptions - Проверка функция возвращает корректные описания для
# каждой транзакции.
# Тест генератора
def test_transaction_descriptions(fix_transactions):
    try:
        generator = transaction_descriptions(fix_transactions)
        assert next(generator) == "Перевод организации"
        assert next(generator) == "Перевод со счета на счет"
        assert next(generator) == "Перевод со счета на счет"
        assert next(generator) == "Перевод с карты на карту"
        assert next(generator) == "Перевод организации"
        assert next(generator) == "Список словарей закончился"
    except StopIteration:
        print("StopIteration")


# Пустой список словарей
def test_transaction_descriptions1():
    try:
        generator = transaction_descriptions([])
        assert next(generator) == "Список словарей закончился"
    except StopIteration:
        print("StopIteration")


# Параметаризация
@pytest.mark.parametrize(
    "value, expected",
    [
        (1, "Перевод организации"),
        (2, "Перевод со счета на счет"),
        (3, "Перевод со счета на счет"),
        (4, "Перевод с карты на карту"),
        (5, "Перевод организации"),
        (6, "Список словарей закончился"),
    ],
)
def test_transaction_descriptions_p(value, expected):
    try:
        result = transaction_descriptions(date_transactions)
        for i in range(value):
            answer_ = next(result)
        assert answer_ == expected
    except StopIteration:
        print("StopIteration")


# card_number_generator - тест правильные ли номера карт в заданном диапазоне.
# Корректность форматирования номеров карт. Обрабатывает крайние значения диапазона.
# Тест генератора
def test_card_number_generator0():
    try:
        generator = card_number_generator(550, 555)
        assert next(generator) == "0000 0000 0000 0550"
        assert next(generator) == "0000 0000 0000 0551"
        assert next(generator) == "0000 0000 0000 0552"
        assert next(generator) == "0000 0000 0000 0553"
        assert next(generator) == "0000 0000 0000 0554"
        assert next(generator) == "0000 0000 0000 0555"
        assert next(generator) == "Заданный диапазон исчерпан!"
    except StopIteration:
        print("StopIteration")


# Параметаризация
@pytest.mark.parametrize(
    "value, expected", [(3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]), (-551, [])]
)
def test_card_number_generator1(value, expected):
    try:
        result = list(card_number_generator(1, value))
        assert result == expected
    except StopIteration:
        print("StopIteration")


def test_card_number_generator2():
    try:
        generator = card_number_generator(550, 10000000000000000)
        assert next(generator) == "Введен неверный диапазон!"
    except StopIteration:
        print("StopIteration")


def test_card_number_generator3():
    try:
        generator = card_number_generator(-5, 1000)
        assert next(generator) == "Введен неверный диапазон!"
    except StopIteration:
        print("StopIteration")


def test_card_number_generator4():
    try:
        generator = card_number_generator(125, 120)
        assert next(generator) == "Введен неверный диапазон!"
    except StopIteration:
        print("StopIteration")
