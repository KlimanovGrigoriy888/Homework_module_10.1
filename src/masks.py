from src.logger import setup_logging

# Создаем логер для masks.py
masks_get_mask_card_number_logger = setup_logging("module-masks/app.get_mask_card_number")
masks_get_mask_account_logger = setup_logging("module-masks/app.get_mask_account")


def get_mask_card_number(cart_number: str) -> str:
    """Функция получает номер банковской карты и отображает в формате XXXX XX** **** XXXX"""
    masks_get_mask_card_number_logger.info("Начало работы функции...")

    cart_number_string = str(cart_number)
    if not cart_number_string.isdigit():
        masks_get_mask_card_number_logger.error("Ошибка ввода 'Не правильно ввели данные'")
        raise ValueError("Не правильно ввели данные карты")
    else:
        masks_get_mask_card_number_logger.info("Возврат результата работы функции 'маска банковской карты'")
        return f"{cart_number_string[0:4]} {cart_number_string[4:6]}** **** {cart_number_string[12:]}"


def get_mask_account(bank_account: str) -> str:
    """Функция получает номер банковского счета и отображает в формате **XXXX"""
    masks_get_mask_account_logger.info("Начало работы функции...")

    bank_account_string = str(bank_account)
    if not bank_account.isdigit():
        masks_get_mask_account_logger.error("Ошибка ввода 'Не правильно ввели данные аккаунта'")
        raise ValueError("Не правильно ввели данные аккаунта")
    else:
        masks_get_mask_account_logger.info("Возврат результата работы функции 'маска банковского аккаунта'")
        return f"**{bank_account_string[-4:]}"


if __name__ == "__main__":
    print(get_mask_account("8990922113665229"))
    print(get_mask_card_number("8990922113665229"))
