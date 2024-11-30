def filter_by_currency(transaction_list: list, currency: str = "USD"):
    """Функция возвращаeт итератор, который поочередно выдает транзакции,
           где валюта операции соответствует заданной, по умолчанию USD"""

    x = 0
    while True:
        if x == len(transaction_list):
            break
        operation = transaction_list[x]
        operation_currency = operation["operationAmount"]["currency"]
        #print(operation_currency)
        if operation_currency["code"] == currency:
            yield operation
        x += 1


def transaction_descriptions(transaction_list: list) -> str:
    """Генератор, который принимает список словарей с транзакциями
           и возвращает описание каждой операции по очереди."""

    x = 0
    while True:
        operation = transaction_list[x]["description"]
        yield operation
        x += 1


def card_number_generator(start: int = 1, stop: int = 10):
    """Генератор, который выдает номера банковских карт
         в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
           Генератор может сгенерировать номера карт в заданном диапазоне
             где start - начало, stop - окончание диапазана."""


    if start > 0 and stop <= 9999999999999999: #проверка на диапазон вводных данных
        num_card = start
        while True:
            sample = '0000000000000000'
            card_num_str = sample[0:16-len(str(num_card))] + str(num_card)
            card_num_mask = " ".join(card_num_str[i * 4: i * 4 + 4] for i in range(4))
            yield card_num_mask
            num_card += 1
            if num_card > stop :
                break
    else:
        print('Введен неверный диапазон!')