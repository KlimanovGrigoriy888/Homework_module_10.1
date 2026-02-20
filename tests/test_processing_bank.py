import pytest

from src.processing_bank import process_bank_search


@pytest.fixture
def my_list_from_json():
    return [{'id': 207126257, 'state': 'EXECUTED', 'date': '2019-07-15T11:47:40.496961',
             'operationAmount': {'amount': '92688.46', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Открытие вклада', 'to': 'Счет 35737585785074382265'},
            {'id': 957763565, 'state': 'EXECUTED', 'date': '2019-01-05T00:52:30.108534',
             'operationAmount': {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод со счета на счет', 'from': 'Счет 46363668439560358409',
             'to': 'Счет 18889008294666828266'},
            {'id': 710136990, 'state': 'CANCELED', 'date': '2018-08-17T03:57:28.607101',
             'operationAmount': {'amount': '66906.45', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'Maestro 1913883747791351',
             'to': 'Счет 11492155674319392427'},
            {'id': 232222017, 'state': 'EXECUTED', 'date': '2018-07-06T22:32:10.495465',
             'operationAmount': {'amount': '37160.27', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод с карты на карту', 'from': 'Visa Classic 4062745111784804',
             'to': 'Maestro 8602249654751155'},
            ]


@pytest.mark.parametrize("state_select, expected_result",
                         [('Перевод с карты на карту',
                           [{'id': 232222017, 'state': 'EXECUTED', 'date': '2018-07-06T22:32:10.495465',
                             'operationAmount': {'amount': '37160.27', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                             'description': 'Перевод с карты на карту', 'from': 'Visa Classic 4062745111784804',
                             'to': 'Maestro 8602249654751155'}]),
                          ('Перевод организации', [
                              {'id': 710136990, 'state': 'CANCELED', 'date': '2018-08-17T03:57:28.607101',
                               'operationAmount': {'amount': '66906.45', 'currency': {'name': 'USD', 'code': 'USD'}},
                               'description': 'Перевод организации', 'from': 'Maestro 1913883747791351',
                               'to': 'Счет 11492155674319392427'}]),
                          ('Перевод со счета на счет', [
                              {'id': 957763565, 'state': 'EXECUTED', 'date': '2019-01-05T00:52:30.108534',
                               'operationAmount': {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                               'description': 'Перевод со счета на счет', 'from': 'Счет 46363668439560358409',
                               'to': 'Счет 18889008294666828266'}]),
                          ('Открытие вклада', [
                              {'id': 207126257, 'state': 'EXECUTED', 'date': '2019-07-15T11:47:40.496961',
                               'operationAmount': {'amount': '92688.46', 'currency': {'name': 'USD', 'code': 'USD'}},
                               'description': 'Открытие вклада', 'to': 'Счет 35737585785074382265'}]),
                          ])
def test_process_bank_json_valid(my_list_from_json, state_select, expected_result):
    assert process_bank_search(my_list_from_json, state_select) == expected_result


@pytest.fixture
def my_list_from_csv():
    return [
        {'id': 5380041.0, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': 23789.0,
         'currency_name': 'Peso', 'currency_code': 'UYU', 'from': None, 'to': 'Счет 23294994494356835683',
         'description': 'Открытие вклада'},
        {'id': 4813301.0, 'state': 'EXECUTED', 'date': '2021-11-02T13:32:15Z', 'amount': 15080.0,
         'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Счет 65547878890984510340',
         'to': 'Счет 91457207307678002163', 'description': 'Перевод со счета на счет'},
        {'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0,
         'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
         'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
        {'id': 3176764.0, 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z', 'amount': 16652.0,
         'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Mastercard 8387037425051294',
         'to': 'American Express 5556525473658852', 'description': 'перевод с карты на карту'},
    ]


@pytest.mark.parametrize("state_select, expected_result",
                         [('Перевод с карты на карту',
                           [{'id': 3176764.0, 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z', 'amount': 16652.0,
                             'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Mastercard 8387037425051294',
                             'to': 'American Express 5556525473658852', 'description': 'перевод с карты на карту'}]),
                          ('Перевод организации', [
                              {'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0,
                               'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
                               'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}]),
                          ('Перевод со счета на счет', [
                              {'id': 4813301.0, 'state': 'EXECUTED', 'date': '2021-11-02T13:32:15Z', 'amount': 15080.0,
                               'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Счет 65547878890984510340',
                               'to': 'Счет 91457207307678002163', 'description': 'Перевод со счета на счет'}]),
                          ('Открытие вклада', [
                              {'id': 5380041.0, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': 23789.0,
                               'currency_name': 'Peso', 'currency_code': 'UYU', 'from': None,
                               'to': 'Счет 23294994494356835683',
                               'description': 'Открытие вклада'}]),
                          ])
def test_process_bank_csv_valid(my_list_from_csv, state_select, expected_result):
    assert process_bank_search(my_list_from_csv, state_select) == expected_result


@pytest.fixture
def my_list_from_excel():
    return [
        {'id': 3358030.0, 'state': 'EXECUTED', 'date': '2023-01-31T13:51:50Z', 'amount': 31030.0,
         'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': None, 'to': 'Счет 70684228258616543122',
         'description': 'Открытие вклада'},
        {'id': 3461845.0, 'state': 'EXECUTED', 'date': '2020-09-14T23:29:55Z', 'amount': 17452.0,
         'currency_name': 'Peso', 'currency_code': 'CLP', 'from': 'Счет 49442217043108853069',
         'to': 'Счет 37821946274775720954', 'description': 'Перевод со счета на счет'},
        {'id': 151337.0, 'state': 'CANCELED', 'date': '2020-10-28T07:47:54Z', 'amount': 30324.0,
         'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Visa 2858643810193921',
         'to': 'Счет 73049787529893930779', 'description': 'Перевод организации'},
        {'id': 1590900.0, 'state': 'CANCELED', 'date': '2020-02-19T08:06:07Z', 'amount': 26493.0,
         'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'American Express 3307595602334148',
         'to': 'Mastercard 2435250807815654', 'description': 'Перевод с карты на карту'},
    ]


@pytest.mark.parametrize("state_select, expected_result",
                         [('Перевод с карты на карту',
                           [{'id': 1590900.0, 'state': 'CANCELED', 'date': '2020-02-19T08:06:07Z', 'amount': 26493.0,
                             'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY',
                             'from': 'American Express 3307595602334148',
                             'to': 'Mastercard 2435250807815654', 'description': 'Перевод с карты на карту'}]),
                          ('Перевод организации', [
                              {'id': 151337.0, 'state': 'CANCELED', 'date': '2020-10-28T07:47:54Z', 'amount': 30324.0,
                               'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY',
                               'from': 'Visa 2858643810193921',
                               'to': 'Счет 73049787529893930779', 'description': 'Перевод организации'}]),
                          ('Перевод со счета на счет', [
                              {'id': 3461845.0, 'state': 'EXECUTED', 'date': '2020-09-14T23:29:55Z', 'amount': 17452.0,
                               'currency_name': 'Peso', 'currency_code': 'CLP', 'from': 'Счет 49442217043108853069',
                               'to': 'Счет 37821946274775720954', 'description': 'Перевод со счета на счет'}]),
                          ('Открытие вклада',
                           [{'id': 3358030.0, 'state': 'EXECUTED', 'date': '2023-01-31T13:51:50Z', 'amount': 31030.0,
                             'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': None,
                             'to': 'Счет 70684228258616543122',
                             'description': 'Открытие вклада'}])
                          ])
def test_process_bank_excel_valid(my_list_from_excel, state_select, expected_result):
    assert process_bank_search(my_list_from_excel, state_select) == expected_result
