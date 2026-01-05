def get_mask_card_number(cart_number: str) -> str:
    """Функция получает номер банковской карты и отображает в формате XXXX XX** **** XXXX"""

    cart_number_string = str(cart_number)

    return f"{cart_number_string[0:4]} {cart_number_string[4:6]}** **** {cart_number_string[12:]}"


if __name__ == "__main__":
    print(get_mask_card_number("8990922113665229"))


def get_mask_account(bank_account: str) -> str:
    """Функция получает номер банковского счета и отображает в формате **XXXX"""

    bank_account_string = str(bank_account)

    return f"**{bank_account_string[-4:]}"


if __name__ == "__main__":
    print(get_mask_account("64686473678894779589"))
