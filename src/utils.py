import json
from json import JSONDecodeError
import os
from src.external_api import get_course_curensy

from tests.test_generators import transactions

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)),"data", "operations.json")

def get_transactions(path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as data_file:
        try:
            operations = json.load(data_file)
            return operations
        except JSONDecodeError:
            print("Ошибка декодирования файла")
            return []


def get_amount_transactions(transactions: dict[int]) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму этой транзакции (amount) в рублях, тип данных —
float. Если транзакция была в USD или EUR, происходит обращение к функции конвертации в модуле external_api для
получения текущего курса валют и конвертации суммы операции в рубли"""
    request_by_course_curensy = get_course_curensy()
    for transaction in transactions:
        get_currency_transaction = transaction.get("operationAmount",{}).get("currency",{}).get("code")
        get_amount_transaction = transaction.get("operationAmount",{}).get("amount")
        if get_currency_transaction == 'RUB': # Операция возврата если валюта рубль.
            return get_amount_transaction
        else: # Операция возврата если валюта не рубль.
            target_exchange_rate_for_rub = request_by_course_curensy.get("rates").get(get_currency_transaction)
            if target_exchange_rate_for_rub == None:
                continue
            target_convert_curency = round((float(get_amount_transaction) * float(target_exchange_rate_for_rub)), 2)
            return target_convert_curency




if __name__ == "__main__":
    transactions = get_transactions(PATH_TO_FILE)
    print(transactions)
    print(get_amount_transactions([{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]))
