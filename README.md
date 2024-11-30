# Проэкт ВИДЖЕТ
## Описание:
Это виджет, который показывает несколько последних успешных банковских операций клиента.
## Установка:

1. Клонируйте репозиторий:
```shell
https://gist.github.com/bzvyagintsev/0c4adf4403d4261808d75f9576c814c2
```
2. Установка зависимостей:
```shell
pip install -r requirements.txt
```
## Использование:
Функции вызываются по мере необходимости из пакетов processing и widget лежащих в папки src.

### Модуль: masks.py

get_mask_card_number(card_number) - Функция принимает на вход номер карты и возвращает ее маску. В случаи ошибки возвращает ошибку.

*пример:*
```shell
print(get_mask_card_number(7000792289606361))
```
*результат* -> 7000 79** **** 6361

get_mask_account(account) - Функция принимает на вход номер счета и возвращает его маску. В случаи ошибки возвращает ошибку.

*пример:*
```shell
print(get_mask_account(73654108430135874305))
```
*результат* -> **4305

### Модуль: processing.py

filter_by_state(list, state_key) - Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
*пример:*
```shell
# со статусом по умолчанию 'EXECUTED'
list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(filter_by_state(list))
```
*результат* -> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

```shell
# со статусом 'CANCELED'
list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(filter_by_state(list,'CANCELED'))
```
*результат* ->  [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

sort_by_date(list, True) - Функция которая принимает список словарей и необязательный параметр, задающий порядок сортировки по дате False/True (по умолчанию — возростание(True))

*пример*
```shell
# со статусом по умолчанию(True)
list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(sort_by_date(list))
```
*результат* -> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

```shell
# со статусом по умолчанию(False)
list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(sort_by_date(list, False))
```
*результат* -> [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

### Модуль: widget.py

mask_account_card(account) - Возвращать строку с замаскированным номером. Для карт и счетов используйте разные типы маскировки.

*пример:*
```shell
# Пример для карты
print(mask_account_card("Visa Platinum 7000792289606361"))
```
*результат* -> Visa Platinum 7000 79** **** 6361

```shell
# Пример для счета
print(mask_account_card("Visa Platinum 73654108430135874305"))
```
*результат* -> Счет **4305

get_date(date) - Возвращает из строки дату в формате: День.Месяц.Год

*пример:*
```shell
print(get_date("2024-03-11T02:26:18.671407"))
```
*результат* -> 11.03.2024

### Модуль: generators

filter_by_currency(list,currency) - функция, которая принимает на вход список словарей, представляющих транзакции.(list)
Возвращаeт итератор, который поочередно выдает транзакции,
где валюта операции соответствует заданной(currency), по умолчанию USD.

*пример:*
```shell
data_s = [
{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },
{
          "id": 939717896,
          "state": "EXECUTED",
          "date": "2019-09-27T12:17:43.425572",
          "operationAmount": {
              "amount": "2588.17",
              "currency": {
                  "name": "RUB",
                  "code": "RUB"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106785213657995148",
          "to": "Счет 11776613755963325672"
      },
      {
              "id": 1422612587,
              "state": "EXECUTED",
              "date": "2022-07-11T20:12:25.206878",
              "operationAmount": {
                  "amount": "12457.23",
                  "currency": {
                      "name": "RUB",
                      "code": "RUB"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 12589645243227456872",
              "to": "Счет 75632675383060288721"
       }
]

filter_by_curr = filter_by_currency(data_s, 'USD')
print(next(filter_by_curr))
```
*Результат* -> {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}

transaction_descriptions(list) - Генератор, который принимает список словарей с транзакциями 
    и возвращает описание каждой операции по очереди.


*пример:(за входящие данные возьмем предыдущий список словарей data_s)* 
```shell
data_s = [
{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },
{
          "id": 939717896,
          "state": "EXECUTED",
          "date": "2019-09-27T12:17:43.425572",
          "operationAmount": {
              "amount": "2588.17",
              "currency": {
                  "name": "RUB",
                  "code": "RUB"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106785213657995148",
          "to": "Счет 11776613755963325672"
      },
      {
              "id": 1422612587,
              "state": "EXECUTED",
              "date": "2022-07-11T20:12:25.206878",
              "operationAmount": {
                  "amount": "12457.23",
                  "currency": {
                      "name": "RUB",
                      "code": "RUB"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 12589645243227456872",
              "to": "Счет 75632675383060288721"
       }
]

descriptions = transaction_descriptions(data_s)
print(next(descriptions))
```
*Результат* -> Перевод организации

card_number_generator(start, stop) - генератор, который выдает номера банковских карт в формате
XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать номера карт 
в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
Генератор принимает начальное (start) и конечное значения (stop) для генерации диапазона номеров.

*пример:* 
```shell
for card_number in card_number_generator(1009458753721699, 1009458753721703):
    print(card_number)
```
*Результат* -> 

1009 4587 5372 1699
1009 4587 5372 1700
1009 4587 5372 1701
1009 4587 5372 1702
1009 4587 5372 1703



## Тестирование модулей
тесты находятся в дериктории tests
## Запуск тестирования 
```shell
poetry run pytest --cov
```
или
``` shell 
pytest --cov=src --cov-report=html
```
 — чтобы сгенерировать отчет о покрытии в HTML-формате, где 
src
 — пакет c модулями, которые тестируем. Отчет будет сгенерирован в папке 
htmlcov
 и храниться в файле с названием 
index.html
.

## Модуль masks
### Функция get_mask_card_number:
1. Тестирование правильности маскирования номера карты.
2. Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и нестандартные длины номеров.
3. Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.

### Функция get_mask_account:
1. Тестирование правильности маскирования номера счета.
2. Проверка работы функции с различными форматами и длинами номеров счетов.
3. Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины.

## Модуль widget
### Функция mask_account_card:
1. Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
2. Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
3. естирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.

### Функция get_data:
1. Тестирование правильности преобразования даты.
2. Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
3. Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.

## Модуль processing
### Функция filter_by_state:
1. Тестирование фильтрации списка словарей по заданному статусу state.
2. Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
3. Параметризация тестов для различных возможных значений статуса state.

### Функция sort_by_date:
1. Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
2. Проверка корректности сортировки при одинаковых датах.
3. Тесты на работу функции с некорректными или нестандартными форматами дат.

## Модуль generators
### Функция filter_by_currency:
1. Тесты, проверяющие, что функция корректно фильтрует транзакции по заданной валюте.
2. Проверка, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют.
3. Проверка на то, что генератор не завершается ошибкой при обработке пустого списка или списка без соответствующих валютных операций.


### Функция transaction_descriptions:
1. Проверка, что функция возвращает корректные описания для каждой транзакции.
2. Тест на работу функции с различным количеством входных транзакций, включая пустой список.

### Функция card_number_generator:
1. Тесты, которые проверяют, что генератор выдает правильные номера карт в заданном диапазоне.
2. Корректность форматирования номеров карт.
3. Проверка на то, что генератор корректно обрабатывает крайние значения диапазона и правильно завершает генерацию.

## Документация:

## Лицензия: 

Этот проект учебный