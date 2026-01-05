import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("cart_number, expected", [(8990922113665229, "8990 92** **** 5229"),
                                                   ("8990922113665229555", "8990 92** **** 5229555"),
                                                   ("8990922113665229", "8990 92** **** 5229"),
                                                   ("6831982476737656", "6831 98** **** 7656"),
                                                   (""," ** **** ")])
def test_get_mask_card_number(cart_number, expected):
    assert get_mask_card_number(cart_number) == expected


@pytest.mark.parametrize("account_number, expected", [(6468647367889, "**7889"),
                                                      (64686473678894779589, "**9589"),
                                                      ("64686473678894779589555", "**9555"),
                                                      ("64686473678894779589", "**9589"),
                                                   ("35383033474447895560", "**5560"),
                                                      ("","**")])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


