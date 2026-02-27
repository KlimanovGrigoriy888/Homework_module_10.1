import os
from typing import Iterable, Any

from src.external_files import read_csv, read_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.processing_bank import process_bank_search, process_bank_operations
from src.utils import get_transactions
from src.widget import get_date, mask_account_card

PATH_TO_FILE_JSON = os.path.join(os.path.dirname(__file__), "data", "operations.json")
PATH_TO_FILE_CSV = os.path.join(os.path.dirname(__file__), "data", "transaction.csv")
PATH_TO_FILE_XLSX = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")

SORT_KEY: bool = False
LIST_TRANSACTIONS: list[dict] = []
FILTERED_TRANSACTIONS: list[dict] = []
sort_list_by_date: list[dict] = []
sort_iter_by_currency: Iterable[dict[Any, Any]]
sort_list_by_currency: list[dict] = []
date_transaction: Any | None


def main() -> None:
    """ Функция обрабатывает банковские транзакций из файлов в папке /data, производит выборку по типу файла, фильтрацию
    по статусу операции, далее по выбору сортировку транзакций по возрастанию или по убыванию, далее выборку
     по рублевым транзакциям или нет, далее по выбору выборку по слову в транзакции. Возвращает список выбранных
      транзакций с информацией с датой, виду транзакции, с масками счета или карты и суммой. """
    global LIST_TRANSACTIONS, FILTERED_TRANSACTIONS, sort_list_by_currency, \
        sort_iter_by_currency, sort_list_by_date, SORT_KEY
    while True:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями")
        input_choice_file = input('''
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
Пользователь: ''')
        if input_choice_file == "1":
            LIST_TRANSACTIONS = get_transactions(PATH_TO_FILE_JSON)
            break
        elif input_choice_file == "2":
            LIST_TRANSACTIONS = read_csv(PATH_TO_FILE_CSV)
            break
        elif input_choice_file == "3":
            LIST_TRANSACTIONS = read_excel(PATH_TO_FILE_XLSX)
            break
        else:
            print("Ошибка! Неверный статус. Попробуйте еще раз.")
            continue
    # print(LIST_TRANSACTIONS)

    valid_response_1 = False
    while not valid_response_1:
        user_response = input('''
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
Пользователь: ''')
        print(f"Операции отфильтрованы по статусу {user_response}")
        if not user_response:
            return None
        elif user_response in ["EXECUTED", "CANCELED", "PENDING"]:
            FILTERED_TRANSACTIONS = filter_by_state(LIST_TRANSACTIONS, state_select=user_response)
            valid_response_1 = True
        else:
            print(f"Статус операции {user_response} недоступен")
    if FILTERED_TRANSACTIONS == []:
        print("Транзакции не найдены")
        return None
    # print(FILTERED_TRANSACTIONS)

    valid_response_2 = False
    while not valid_response_2:
        user_input_sort_by_date = input('''
Отсортировать операции по дате? Да/Нет
Пользователь: ''').lower()
        if user_input_sort_by_date == "да":
            valid_response_3 = False
            while not valid_response_3:
                user_input_sort_by_rise = input('''
Отсортировать "по возрастанию" или "по убыванию"?
Пользователь: ''').lower()
                if user_input_sort_by_rise == "по возрастанию":
                    SORT_KEY = False
                    valid_response_3 = True
                elif user_input_sort_by_rise == "по убыванию":
                    SORT_KEY = True
                    valid_response_3 = True
                else:
                    print("Ошибка! Введите 'по возрастанию' или 'по убыванию'.")
            sort_list_by_date = sort_by_date(FILTERED_TRANSACTIONS, key_sort=SORT_KEY)
            valid_response_2 = True
        elif user_input_sort_by_date == "нет":
            sort_list_by_date = FILTERED_TRANSACTIONS
            valid_response_2 = True
        else:
            print("Ошибка! Ответьте 'Да' или 'Нет'.")
    # print(sort_list_by_date)

    valid_response_4 = False
    while not valid_response_4:
        user_input_choice_currency = input('''
Выводить только рублевые транзакции? Да/Нет
Пользователь: ''').lower()
        if user_input_choice_currency == "да":
            sort_iter_by_currency = filter_by_currency(sort_list_by_date, "RUB")
            valid_response_4 = True
        elif user_input_choice_currency == "нет":
            sort_iter_by_currency = filter_by_currency(sort_list_by_date, "USD")
            valid_response_4 = True
        else:
            print("Ошибка! Ответьте 'Да' или 'Нет'.")
    sort_list_by_currency = list(sort_iter_by_currency)
    # print(sort_list_by_currency)

    valid_response_5 = False
    while not valid_response_5:
        user_input_filtered_by_word = input('''
Отфильтровать список транзакций по определенному слову в описании? Да/Нет
Пользователь: ''').lower()
        if user_input_filtered_by_word == "да":
            valid_response_6 = False
            while not valid_response_6:
                user_input_filtered_by_word = input("""
Введите искомое слово: Перевод с карты на карту, Перевод организации, Перевод со счета на счет, Открытие вклада
Пользователь: """).lower()
                if user_input_filtered_by_word in ['перевод с карты на карту', 'перевод организации',
                                                   'перевод со счета на счет', 'открытие вклада']:
                    sorted_list_by_word = process_bank_search(sort_list_by_currency, user_input_filtered_by_word)
                    valid_response_6 = True
                else:
                    print("Ошибка! Неверный выбор. Попробуйте еще раз.")
            sorted_list_by_description = sorted_list_by_word
            valid_response_5 = True
        elif user_input_filtered_by_word == "нет":
            sorted_list_by_description = sort_list_by_currency
            valid_response_5 = True
        else:
            print("Ошибка! Ответьте 'Да' или 'Нет'.")
    # print(sorted_list_by_description)

    all_description = ['Перевод с карты на карту', 'Перевод организации',
                       'Перевод со счета на счет', 'Открытие вклада']
    target_filtered_list = process_bank_operations(sorted_list_by_description, all_description)
    print("Распечатываю итоговый список транзакций...")
    sum_value = 0
    for operation, value in target_filtered_list.items():
        if value:
            sum_value += int(value)
    print(f"Всего банковских операций в выборке: {sum_value}")

    for transaction in sorted_list_by_description:
        raw_date = transaction.get("date", "")
        date_transaction = get_date(str(raw_date))

        raw_to = transaction.get("to", "")
        transaction_description_to = mask_account_card(str(raw_to))

        description_transaction = transaction.get("description", "")

        op_amount = transaction.get("operationAmount")
        if isinstance(op_amount, dict):
            # Для JSON структуры
            transaction_amount = op_amount.get("amount", "")
        else:
            # Для CSV и EXCEL структуры
            transaction_amount = transaction.get("amount")

        if description_transaction == 'Открытие вклада':
            print(f"{date_transaction} {description_transaction}\n"
                  f"{transaction_description_to}\n"
                  f"Сумма {transaction_amount}")
        else:
            raw_from = transaction.get("from", "")
            transaction_description_from = mask_account_card(str(raw_from))
            print(f"{date_transaction} {description_transaction}\n"
                  f"{transaction_description_from} -> {transaction_description_to}\n"
                  f"Сумма {transaction_amount}")


if __name__ == "__main__":
    main()
