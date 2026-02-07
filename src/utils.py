import json
import os
from json import JSONDecodeError

from src.external_api import get_course_currency

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")


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


def get_amount_transactions(transactions: list[dict]) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму этой транзакции (amount) в рублях, тип данных —
    float. Если транзакция была в USD или EUR, происходит обращение к функции конвертации в модуле external_api для
    получения текущего курса валют и конвертации суммы операции в рубли"""
    status, request_by_course_currency = get_course_currency()
    print(status, request_by_course_currency)
    if not status:
        raise Exception("Filed get currency rate")
    if not transactions:
        raise TypeError("Filed not input data")
    for transaction in transactions:
        get_currency_transaction = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        get_amount_transaction = transaction.get("operationAmount", {}).get("amount")
        if get_currency_transaction is None:
            raise KeyError("Filed not key for get_currency_transaction")
        if get_amount_transaction is None:
            raise KeyError("Filed not key for get_amount_transaction")
        if get_currency_transaction == "RUB":  # Операция возврата если валюта рубль.
            return get_amount_transaction
        else:  # Операция возврата если валюта не рубль.
            target_exchange_rate_for_rub = request_by_course_currency.get("rates").get(get_currency_transaction)
            if target_exchange_rate_for_rub is None:
                raise KeyError("Filed not key for target_exchange_rate_for_rub")
            target_convert_currency = round((float(get_amount_transaction) * float(target_exchange_rate_for_rub)), 2)
            return target_convert_currency


# if __name__ == "__main__":
#     transactions = get_transactions(PATH_TO_FILE)
#     print(transactions)
#     print(get_amount_transactions([{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
#                                     'operationAmount': {'amount': '31957.58',
#                                                         'currency': {'name': 'руб.', 'code': 'RUB'}},
#                                     'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
#                                     'to': 'Счет 64686473678894779589'}]))
