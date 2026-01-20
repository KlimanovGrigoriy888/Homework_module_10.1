from typing import Any, Iterable


def filter_by_currency(list_transactions: list[dict], currency: str) -> Iterable[dict[Any, Any]]:
    """Функция принимает на вход список словарей, представляющих транзакции и возвращает генераторный объект,
    который возвращает транзакции, где валюта операции соответствует заданной (например, USD)."""
    if list_transactions == [] or currency == '':
        raise StopIteration
    else:
        result = (x for x in list_transactions if x["operationAmount"]["currency"]["code"] == currency)
        return result


def transaction_descriptions(list_transactions: list[dict]) -> Iterable[Any]:
    """Генератор принимает на вход список словарей с транзакциями и возвращает генераторный объект,
     который возвращает описание каждой операции по очереди."""
    if list_transactions == []:
        raise StopIteration and RuntimeError
    else:
        for x in list_transactions:
            if not x["description"]:
                raise KeyError
            else:
                yield x["description"]


def card_number_generator(start_number: int, stop_number: int) -> Iterable:
    """Функция генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Принимает на вход начальное и конечное значение генерации диапазонов номеров карт. Генератор может сгенерировать
    номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    if str(start_number).isalpha() or str(stop_number).isalpha():
        raise TypeError
    else:
        for gen_number in range(start_number, stop_number + 1):
            if gen_number <= 9999999999999999 and gen_number > 0:
                gen_number_str = f"{gen_number:016d}"
                result_number_masks = (
                    f"{gen_number_str[:4]} {gen_number_str[4:8]} {gen_number_str[8:12]} {gen_number_str[12:16]}"
                )
            yield result_number_masks


if __name__ == "__main__":
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(3):
        print(next(iter(usd_transactions)))

    descriptions = transaction_descriptions(transactions)
    for _ in range(3):
        print(next(iter(descriptions)))

    for card_number in card_number_generator(1, 5):
        print(card_number)
