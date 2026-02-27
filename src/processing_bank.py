import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка в 'description' """
    # Если принимаем пустой список или нет искомого слова возвращаем пустой список
    if not data or not search:
        return []
        # Находим нужную строку в списке с помощью регулярного выражения
    pattern = re.compile(rf"\b{search}\b", re.IGNORECASE)
    result = []

    for transaction in data:
        # Извлекаем транзакцию
        description = transaction.get('description')
        if not description:
            continue
        try:
            if pattern.fullmatch(description):
                result.append(transaction)
        except KeyError:
            continue
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций, возвращает
     словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    if not data or not categories:
        return {}
    # Создаем объект Counter в котором будут ключи — это названия категорий, а значения — это количество операций.
    category_count: Counter = Counter()
    for category in categories:
        # Используем внешнюю функцию для фильтрации списка операций по категории.
        list_for_category = process_bank_search(data, category)
        # Добавляем информацию по ключу — это названия категорий и значению — это количество операций
        category_count[category] += len(list_for_category)

    return dict(category_count)


if __name__ == "__main__":
    list_transactions = [
        {'id': 3967324.0, 'state': 'EXECUTED', 'date': '2021-05-22T07:46:10Z', 'amount': 30809.0,
         'currency_name': 'Peso', 'currency_code': 'PHP', 'from': None, 'to': 'Счет 99143269778241825075',
         'description': 'Открытие вклада'},
        {'id': 5515847.0, 'state': 'EXECUTED', 'date': '2021-08-30T06:11:23Z', 'amount': 18687.0,
         'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Mastercard 3924599516675344',
         'to': 'Visa 4023206149439133', 'description': None},
        {'id': 4813301.0, 'state': 'EXECUTED', 'date': '2021-11-02T13:32:15Z', 'amount': 15080.0,
         'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Счет 65547878890984510340',
         'to': 'Счет 91457207307678002163', 'description': 'Перевод со счета на счет'},
        {'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0,
         'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
         'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}
    ]
    name_search = input("Введите искомое слово: ")
    print(process_bank_search(list_transactions, name_search))
#     result_bank_operations = process_bank_operations(list_transactions,
#                                                      ['Перевод с карты на карту', 'Перевод организации',
#                                                       'Перевод со счета на счет',
#                                                       'Открытие вклада'])
# #     sum_value = 0
#     for operation, value in result_bank_operations.items():
#         if value:
#             sum_value += int(value)
#             print(operation, value)
#     print(sum_value)
