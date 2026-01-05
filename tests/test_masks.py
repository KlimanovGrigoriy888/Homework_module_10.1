import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("cart_number, expected", [(8990922113665229, "8990 92** **** 5229"),
                                                   ("8990922113665229555", "8990 92** **** 5229555"),
                                                   ("8990922113665229", "8990 92** **** 5229"),
                                                   ("6831982476737656", "6831 98** **** 7656")])
def test_get_mask_card_number(cart_number, expected):
    assert get_mask_card_number(cart_number) == expected


def test_get_mask_card_number_wrong_date_1():
    with pytest.raises(TypeError):
        assert get_mask_card_number()


def test_get_mask_card_number_wrong_date_2():
    with pytest.raises(ValueError):
        assert get_mask_card_number("ABVG")


@pytest.mark.parametrize("account_number, expected", [("64686473678894779589555", "**9555"),
                                                      ("64686473678894779589", "**9589"),
                                                      ("35383033474447895560", "**5560")])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_wrong_date_1():
    with pytest.raises(TypeError):
        assert get_mask_account()


def test_get_mask_account_wrong_date_2():
    with pytest.raises(ValueError):
        assert get_mask_account("ABVG")


def test_get_mask_account_wrong_date_3():
    with pytest.raises(AttributeError):
        assert get_mask_account(64686473678894779589)
