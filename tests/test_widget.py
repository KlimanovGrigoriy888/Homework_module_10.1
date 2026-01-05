import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("cart_number, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                   ("Счет 64686473678894779589", "Счет **9589"),
                                                   ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                                   ("Visa Classic 6831982476737658",
                                                    "Visa Classic 6831 98** **** 7658"),
                                                   ("Visa Platinum 8990922113665229",
                                                    "Visa Platinum 8990 92** **** 5229"),
                                                   ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                                                   ("Мир 5999414228426353", "Мир 5999 41** **** 6353")])
def test_mask_account_card(cart_number, expected):
    assert mask_account_card(cart_number) == expected


@pytest.mark.parametrize("input_date, expected_date", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                                       ("2025-12-11T02:00:00.000000", "11.12.2025"), ])
def test_get_date(input_date, expected_date):
    assert get_date(input_date) == expected_date


def test_get_date_wrong_type_1():
    with pytest.raises(ValueError):
        assert get_date("2024-03-11T02:26")


def test_get_date_wrong_type_2():
    with pytest.raises(ValueError):
        assert get_date("")


def test_get_date_wrong_type_3():
    with pytest.raises(TypeError):
        assert get_date()
