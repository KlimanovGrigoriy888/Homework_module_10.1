def filter_by_state(list_dict_id: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция принимает на вход список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей,
     содержащий только те словари, у которых ключ state соответствует
      указанному значению."""
    new_list_dict_id = list()
    for id_list in list_dict_id:
        if id_list['state'] == state:
            new_list_dict_id.append(id_list)
    return new_list_dict_id


def sort_by_date(list_dict_id: list[dict], key_sort: bool = True) -> list[dict]:
    """Функция принимает список словарей и параметр сортировку, задающий порядок сортировки
    (по умолчанию — убывание) и возвращает новый список, отсортированный по дате (date)."""
    sort_list_by_date = sorted(list_dict_id, key=lambda x: x['date'], reverse=key_sort)
    return sort_list_by_date


if __name__ == "__main__":
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'EXECUTED'))
# Выход функции со статусом по умолчанию 'EXECUTED'
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], True))

# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
