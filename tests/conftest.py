import pytest


# Фикстуры для test_masks.py
@pytest.fixture
def fix_get_mask_card_number():
    return "7000792289606361"


@pytest.fixture
def fix_get_mask_account():
    return "73654108430135874305"


# Фикстуры для test_widget.py
@pytest.fixture
def fix_mask_account_card():
    return "Maestro 1596837868705199"


@pytest.fixture
def fix_mask_account_card_c():
    return "Счет 35383033474447895560"


@pytest.fixture
def fix_get_date():
    return "2024-03-11T02:26:18.671407"


# Фикстуры для test_processing.py
@pytest.fixture
def fix_filter_by_state():
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
