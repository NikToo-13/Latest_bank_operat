import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import operation_converter

load_dotenv()
keys = os.getenv("API_KEY")
payload = {}
headers = {"apikey": keys}
url = "https://api.apilayer.com/exchangerates_data/convert"


@patch("requests.request")
def test_operation_converter(mock_get):
    """Проверка на работоспособность"""
    mock_get.return_value.json.return_value = {"result": 103.85}
    mock_get.return_value.status_code = 200
    assert operation_converter({"amount": "1", "currency": {"name": "USD", "code": "USD"}}) == 103.85
