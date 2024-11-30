def filter_by_currency(transaction_list: list, currency: str = "USD", x=0):
    """Функция возвращаeт итератор, который поочередно выдает транзакции,
           где валюта операции соответствует заданной, по умолчанию USD"""


    while True:
        if x == len(transaction_list):
            break
        operation = transaction_list[x]
        operation_currency = operation["operationAmount"]["currency"]
        #print(operation_currency)
        if operation_currency["name"] == currency:
            yield operation
        x += 1
