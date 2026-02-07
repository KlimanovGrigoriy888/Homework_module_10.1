from unittest.mock import mock_open, patch

import pytest

from src.utils import get_amount_transactions, get_transactions


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1]')
def test_get_transactions_wrong_json(mock_file, mock_exists):
    mock_exists.return_value = True
    result = get_transactions("dummy_path.json")

    assert result == []


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1}]')
def test_get_transactions(mock_open, mock_exists):
    mock_exists.return_value = True
    path = "dummy_path.json"
    result = get_transactions(path)
    assert result == [{"id": 1}]


@patch("src.utils.get_course_currency")
def test_get_amount_transactions_empty_data(mock_get_currency):
    # Проверка случая, когда НЕ получена транзакция
    mock_get_currency.return_value = True, [{}]

    with pytest.raises(TypeError, match="Filed not input data"):
        get_amount_transactions([])


def test_get_amount_transactions_failed_currency():
    # Проверка случая, когда курс НЕ получен
    with patch("src.utils.get_course_currency") as mock_get_currency:
        mock_get_currency.return_value = False, [{}]

        with pytest.raises(Exception):
            get_amount_transactions(
                [
                    {
                        "id": 441945886,
                        "state": "EXECUTED",
                        "date": "2019-08-26T10:50:58.294041",
                        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                        "description": "Перевод организации",
                        "from": "Maestro 1596837868705199",
                        "to": "Счет 64686473678894779589",
                    }
                ]
            )


@pytest.fixture()
def getting_good_transactions():
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    ]


@patch("src.utils.get_course_currency")
def test_get_amount_transactions_not_rates_in_API(mock_get_currency, getting_good_transactions):
    mock_get_currency.return_value = True, {
        "success": True,
        "timestamp": 1769955604,
        "base": "RUB",
        "date": "2026-02-01",
        "rates": {"1": 0.013093, "2": 0.011045},
    }
    with pytest.raises(KeyError, match="Filed not key for target_exchange_rate_for_rub"):
        get_amount_transactions(getting_good_transactions)


@pytest.fixture()
def getting_transactions_not_course():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб."}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


@patch("src.utils.get_course_currency")
def test_get_amount_transactions_not_course_transaction(mock_get_currency, getting_transactions_not_course):
    mock_get_currency.return_value = True, {
        "success": True,
        "timestamp": 1769955604,
        "base": "RUB",
        "date": "2026-02-01",
        "rates": {"USD": 0.013093, "EUR": 0.011045},
    }
    with pytest.raises(KeyError, match="Filed not key for get_currency_transaction"):
        get_amount_transactions(getting_transactions_not_course)


@pytest.fixture()
def getting_transactions_not_rates():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


@patch("src.utils.get_course_currency")
def test_get_amount_transactions_not_currency_transaction(mock_get_currency, getting_transactions_not_rates):
    mock_get_currency.return_value = True, {
        "success": True,
        "timestamp": 1769955604,
        "base": "RUB",
        "date": "2026-02-01",
        "rates": {"USD": 0.013093, "EUR": 0.011045},
    }
    with pytest.raises(KeyError, match="Filed not key for get_currency_transaction"):
        get_amount_transactions(getting_transactions_not_rates)


@pytest.fixture()
def getting_transactions_not_operation_Amount():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


@patch("src.utils.get_course_currency")
def test_get_amount_transactions_not_operationAmount_transaction(
    mock_get_currency, getting_transactions_not_operation_Amount
):
    mock_get_currency.return_value = True, {
        "success": True,
        "timestamp": 1769955604,
        "base": "RUB",
        "date": "2026-02-01",
        "rates": {"USD": 0.013093, "EUR": 0.011045},
    }
    with pytest.raises(KeyError, match="Filed not key for get_amount_transaction"):
        get_amount_transactions(getting_transactions_not_operation_Amount)
