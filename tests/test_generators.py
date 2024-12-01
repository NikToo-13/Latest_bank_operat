from src.generators import transaction_descriptions, filter_by_currency, card_number_generator


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
    generator = filter_by_currency(fix_transactions, "YAN")
    assert next(generator) == "Список словарей закончился"


# Пустой список словарей
def test_filter_by_currency3():
    generator = filter_by_currency([], "USD")
    assert next(generator) == "Список словарей закончился"


# transaction_descriptions - Проверка функция возвращает корректные описания для
# каждой транзакции.
# Тест генератора
def test_transaction_descriptions(fix_transactions):
    generator = transaction_descriptions(fix_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Список словарей закончился"


# Пустой список словарей
def test_transaction_descriptions1():
    generator = transaction_descriptions([])
    assert next(generator) == "Список словарей закончился"


# card_number_generator - тест правильные ли номера карт в заданном диапазоне.
# Корректность форматирования номеров карт. Обрабатывает крайние значения диапазона.
# Тест генератора
def test_card_number_generator():
    generator = card_number_generator(550, 555)
    assert next(generator) == "0000 0000 0000 0550"
    assert next(generator) == "0000 0000 0000 0551"
    assert next(generator) == "0000 0000 0000 0552"
    assert next(generator) == "0000 0000 0000 0553"
    assert next(generator) == "0000 0000 0000 0554"
    assert next(generator) == "0000 0000 0000 0555"
    assert next(generator) == "Заданный диапазон исчерпан!"


def test_card_number_generator1():
    generator = card_number_generator(550, 10000000000000000)
    assert next(generator) == "Введен неверный диапазон!"


def test_card_number_generator2():
    generator = card_number_generator(-5, 1000)
    assert next(generator) == "Введен неверный диапазон!"


def test_card_number_generator3():
    generator = card_number_generator(125, 120)
    assert next(generator) == "Введен неверный диапазон!"
