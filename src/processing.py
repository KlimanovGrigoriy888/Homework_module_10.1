from datetime import datetime


def filter_by_state(list_dict_id: list[dict], *, state_select: str = 'EXECUTED') -> list[dict]:
    """Функция принимает на вход список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
    указанному значению. """
    if not list_dict_id:
        return []

    new_list_dict_id = []

    state_select_upper = state_select.upper()
    for id_list in list_dict_id:
        # Получаем значение по ключу 'state', если ключа нет — вернется None
        state = id_list.get('state')

        if isinstance(state, str):
            if state.upper() == state_select_upper:
                new_list_dict_id.append(id_list)

    return new_list_dict_id


def sort_by_date(list_dict_id: list[dict], key_sort: bool = True) -> list[dict]:
    """Функция принимает список словарей и параметр сортировку, задающий порядок сортировки
    (по умолчанию True — убывание) и возвращает новый список, отсортированный по дате (date)."""
    try:
        return sorted(
            list_dict_id,
            # Сортируем, превращая строку во временный объект datetime для сравнения
            key=lambda x: datetime.fromisoformat(x['date'].replace('Z', '.000000')),
            reverse=key_sort
        )
    except (KeyError, ValueError, TypeError) as e:
        print(f"Ошибка в данных: {e}")
        return []


# if __name__ == "__main__":
#     PATH_TO_FILE_JSON = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
#     PATH_TO_FILE_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transaction.csv")
#     LIST_TRANSACTIONS = read_csv(PATH_TO_FILE_CSV)
#     print(LIST_TRANSACTIONS)
#     print(filter_by_state(LIST_TRANSACTIONS, state_select="CANCELED"))
    # Выход функции со статусом по умолчанию 'EXECUTED'
    # [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    #  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

    # print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    #                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    #                     {'id': 594226727, 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z'},
    #                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], True))

    # Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
    # [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    #  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    #  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    #  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
