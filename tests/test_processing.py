from src.processing import filter_by_state, sort_by_date

import pytest

#Тест проверки функций filter_by_state, sort_by_date модуля processing.py


datas = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

@pytest.mark.parametrize('value, expected', [
    ('EXECUTED' , [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
     ),
    ('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
     ),
    ('CELED', 'Отсутствуют записи с данным статусом'
     ),
    ('', 'Некоректный статус'
     )
])
def test_filter_by_state(value, expected):
    assert filter_by_state(datas, value) == expected