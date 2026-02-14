import json
import os
from json import JSONDecodeError
from typing import Any, Union, cast

from src.external_api import get_course_currency
from src.logger import setup_logging

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")

# Создаем логер для utils
utils_get_transactions_logger = setup_logging('modul-utils/app.get_transactions')
utils_get_amount_transactions_logger = setup_logging('modul-utils/app.get_amount_transactions')


def get_transactions(path: str) -> list[dict[Any, Any]]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    utils_get_transactions_logger.info("Начало работы функции...")
    if not os.path.exists(path):
        utils_get_transactions_logger.error("Функция не получила путь к файлу с данными о транзакциях, "
                                            "возврат пустого списка")
        return []
    try:
        utils_get_transactions_logger.info("Открытие файла для чтения транзакции")
        with open(path, "r", encoding="utf-8") as data_file:
            utils_get_transactions_logger.info("Чтение данных из файла в формате json")
            operations = json.load(data_file)
            utils_get_transactions_logger.info("Вывод данных из файла в формате json")
            return cast(list[dict[Any, Any]], operations)
    except (FileNotFoundError,JSONDecodeError):
        utils_get_transactions_logger.error("Ошибка декодирования файла json и вывод пустого списка")
        print("Ошибка декодирования файла и вывод пустого списка")
        return []


def get_amount_transactions(transactions: list[dict]) -> float | None | Any:
    """Функция, которая принимает на вход транзакцию и возвращает сумму этой транзакции (amount) в рублях, тип данных —
    float. Если транзакция была в USD или EUR, происходит обращение к функции конвертации в модуле external_api для
    получения текущего курса валют и конвертации суммы операции в рубли"""
    utils_get_amount_transactions_logger.info("Начало работы функции...")
    status, request_by_course_currency = get_course_currency()
    utils_get_amount_transactions_logger.info(f"Получение статуса = {status} запроса по API курса валют")
    print(status, request_by_course_currency)
    if not status:
        utils_get_amount_transactions_logger.error(f"Полученный статус по API = {status}, возвращаем ошибку "
                                                   f"Filed get currency rate")
        raise Exception("Filed get currency rate")
    if not transactions:
        utils_get_amount_transactions_logger.error("Не получена транзакция в функцию, возвращаем ошибку"
                                                   " Filed get currency rate")
        raise TypeError("Filed not input data")
    for transaction in transactions:
        utils_get_amount_transactions_logger.info("Ищем код валюты и сумму из транзакции")
        get_currency_transaction = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        get_amount_transaction = transaction.get("operationAmount", {}).get("amount")
        if get_currency_transaction is None:
            utils_get_amount_transactions_logger.error("Не найден ключ поиска по коду валюты 'code', "
                                                       "исключение Filed not key for get_currency_transaction")
            raise KeyError("Filed not key for get_currency_transaction")
        if get_amount_transaction is None:
            utils_get_amount_transactions_logger.error("Не найден ключ поиска по коду сумма 'amount', "
                                                       "исключение Filed not key for get_currency_transaction")
            raise KeyError("Filed not key for get_amount_transaction")
        if get_currency_transaction == "RUB":  # Операция возврата если валюта рубль.
            utils_get_amount_transactions_logger.info("Возвращаем сумму валюты если код валюты 'RUB'")
            return float(get_amount_transaction)
        else:  # Операция возврата если валюта не рубль.
            rates = request_by_course_currency.get("rates", {})
            target_exchange_rate_for_rub = rates.get(get_currency_transaction)
            if target_exchange_rate_for_rub is None:
                utils_get_amount_transactions_logger.error("Не найден значение курса искомой валюты 'rates' из API"
                                                           "запроса, исключение "
                                                           "Filed not key for get_currency_transaction")
                raise KeyError("Filed not key for target_exchange_rate_for_rub")
            target_convert_currency = round((float(get_amount_transaction) * float(target_exchange_rate_for_rub)), 2)
            utils_get_amount_transactions_logger.info("Возвращаем пересчитанную сумму в рублях если валюта не 'RUB'")
            return float(target_convert_currency)
    # Если цикл for завершился и не сработал ни один return внутри
    raise ValueError("No valid transaction data found in the list")


if __name__ == "__main__":
    transactions = get_transactions(PATH_TO_FILE)
    print(transactions)
    print(get_amount_transactions([{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                                    'operationAmount': {'amount': '31957.58',
                                                        'currency': {'name': 'руб.', 'code': 'RUB'}},
                                    'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                                    'to': 'Счет 64686473678894779589'}]))
