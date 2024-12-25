import os

import requests
from dotenv import load_dotenv

load_dotenv()
keys = os.getenv("API_KEY")


def operation_converter(transaction: list) -> float:
    """функцию, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях,
    тип данных — float. В случии ошибки выводит сообщение и возвращает -1"""
    try:
        payload = {}
        headers = {"apikey": keys}
        transaction_currency = transaction["currency"]["code"]
        if transaction_currency != "RUB":
            to = "RUB"
            froms = transaction_currency
            amount = transaction["amount"]
            url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={froms}&amount={amount}"
            response = requests.request("GET", url, headers=headers, data=payload)
            status_code = response.status_code
            if status_code == 200:
                summ = float(response.json()["result"])
            else:
                print(status_code)
                print(response.reason)
                return -1
        else:
            summ = transaction["amount"]
        return summ
    except Exception:
        return -1
