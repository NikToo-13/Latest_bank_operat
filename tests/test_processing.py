from src.processing import filter_by_state, sort_by_date

import pytest

# Тест проверки функций filter_by_state, sort_by_date модуля processing.py


datas = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


# Словарь с одинаковыми датами
datas1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064531, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 615064541, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 615064551, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Словари с нестондартный датами
datas2 = [
    {"id": 41428829, "state": "EXECUTED", "date": "35/14/2020T18:35:29.512364"},
    {"id": 615064531, "state": "CANCELED", "date": "33/17/2020T08:21:33.419441"},
    {"id": 615064541, "state": "CANCELED", "date": "75/24/2020T08:21:33.419441"},
    {"id": 615064551, "state": "CANCELED", "date": "55/14/2020T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "35/17/2020T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "38/14/2020T02:08:58.425572"},
]

datas3 = [
    {"id": 41428829, "state": "EXECUTED", "date": "abcd-ef-ghT18:35:29.512364"},
    {"id": 615064531, "state": "CANCELED", "date": "abcd-ef-ghT08:21:33.419441"},
    {"id": 615064541, "state": "CANCELED", "date": "abcb-ed-gh0T08:21:33.419441"},
    {"id": 615064551, "state": "CANCELED", "date": "abca-ec-ghT08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "abcc-eb-ghT21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "abce-ea-ghT02:08:58.425572"},
]

datas4 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2020-02-30T18:35:29.512364"},
    {"id": 615064531, "state": "CANCELED", "date": "2020-77-83T08:21:33.419441"},
    {"id": 615064541, "state": "CANCELED", "date": "2020-67-92T08:21:33.419441"},
    {"id": 615064551, "state": "CANCELED", "date": "2020-39-41T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2020-17-68T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2020-84-23T02:08:58.425572"},
]

datas5 = [
    {"id": 41428829, "state": "EXECUTED"},
    {"id": 615064531, "state": "CANCELED"},
    {"id": 615064541, "state": "CANCELED"},
    {"id": 615064551, "state": "CANCELED"},
    {"id": 594226727, "state": "CANCELED"},
    {"id": 939719570, "state": "EXECUTED"},
]


# filter_by_state проверка функции
# фикстура
def test_f_filter_by_state(fix_filter_by_state):
    assert filter_by_state(fix_filter_by_state, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_f_filter_by_state1(fix_filter_by_state):
    assert filter_by_state(fix_filter_by_state, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# параметризация
@pytest.mark.parametrize(
    "value, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("CELED", "Отсутствуют записи с данным статусом"),
        ("", "Некоректный статус"),
    ],
)
def test_filter_by_state(value, expected):
    assert filter_by_state(datas, value) == expected


# Проверка сортировки дат
# sort_by_date проверка функции
# фикстура
def test_f_sort_by_date(fix_sort_by_date):
    assert sort_by_date(fix_sort_by_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# параметризация
@pytest.mark.parametrize(
    "value, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(value, expected):
    assert sort_by_date(datas, value) == expected


# Проверка сортировки одинаковых дат
# sort_by_date проверка функции
# фикстура
def test_f_sort_by_date0(fix_sort_by_date0):
    assert sort_by_date(fix_sort_by_date0) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064531, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064541, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064551, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# параметризация
@pytest.mark.parametrize(
    "value, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064531, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 615064541, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 615064551, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064531, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 615064541, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 615064551, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date1(value, expected):
    assert sort_by_date(datas1, value) == expected


@pytest.mark.parametrize("value, expected", [(True, "Некоректные данные"), (False, "Некоректные данные")])
def test_sort_by_date2(value, expected):
    assert sort_by_date(datas2, value) == expected


@pytest.mark.parametrize("value, expected", [(True, "Некоректные данные"), (False, "Некоректные данные")])
def test_sort_by_date3(value, expected):
    assert sort_by_date(datas3, value) == expected
