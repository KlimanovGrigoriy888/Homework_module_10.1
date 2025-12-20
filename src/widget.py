import re


def mask_account_card(card_account: str) -> str:
    """Принимает на вход даннве типа название карты и ее номер или счет и его номер,
    возвращает их маску типа: Visa Platinum 7000 XX** **** XXXX, Счет **XXXX"""

    text_list_russian = re.findall(r"\b[а-яА-я]+\b", card_account)
    text_list_english = re.findall(r"\b[a-zA-Z]+\b", card_account)
    # print(bool(text_list_russian))
    # print(bool(text_list_english))

    if bool(text_list_russian):
        text_string = " ".join(text_list_russian)
    else:
        text_string = " ".join(text_list_english)
    if bool(text_list_russian):
        number_list = re.findall(r"\d", card_account)
        numbers_string = "".join(number_list)
        result = f"{text_string} **{numbers_string[-4:]}"

    if not bool(text_list_russian):
        number_list = re.findall(r"\d", card_account)
        numbers_string = "".join(number_list)
        result = f"{text_string} {numbers_string[0:4]} {numbers_string[4:6]}** **** {numbers_string[12:]}"

    return result


if __name__ == "__main__":

    print(mask_account_card("Счет 64686473678894779589"))
