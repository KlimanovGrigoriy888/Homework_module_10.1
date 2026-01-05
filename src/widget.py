import re
from datetime import datetime as dt


def mask_account_card(card_account: str) -> str:
    """Принимает на вход данные типа название карты и ее номер или счет и его номер,
    возвращает их маску типа: Visa Platinum 7000 XX** **** XXXX, Счет **XXXX"""

    # Возвращаем из буквенной части card_account, английский или русский текст в виде двух списков слов
    # английских или русских.
    text_list_russian = re.findall(r"\b[а-яА-я]+\b", card_account)
    text_list_english = re.findall(r"\b[a-zA-Z]+\b", card_account)
    # Создаем метку это крилица или нет.
    is_cyrillic = bool(text_list_russian)

    # Возвращаем текст в виде строки, для кирилицы и английского отдельно от метки.
    if is_cyrillic:
        text_string = " ".join(text_list_russian)
    else:
        text_string = " ".join(text_list_english)

    # Фильтруем строку текста по критерию "Счет", опредеяем счет это или карта.
    # Отфильтровываем только цифры из входныех данных и маскируем с помошью функции из модуля masks,
    # выводим маску ответа.
    from src.masks import get_mask_account, get_mask_card_number
    if text_string == "Счет":
        number_list = re.findall(r"\d", card_account)
        numbers_string = "".join(number_list)
        check_mask = get_mask_account(numbers_string)
        result = f"{text_string} {check_mask}"

    if text_string != "Счет":
        number_list = re.findall(r"\d", card_account)
        numbers_string = "".join(number_list)
        cart_mask = get_mask_card_number(numbers_string)
        result = f"{text_string} {cart_mask}"
    return result


def get_date(first_str_date: str) -> str:
    """Принимает строку в формате "2024-03-11T02:26:18.671407" и возвращает "ДД.ММ.ГГГГ"
 ("11.03.2024")"""

    try:
        valid_formatted_date = dt.strptime(first_str_date, "%Y-%m-%dT%H:%M:%S.%f")
        second_date = valid_formatted_date.strftime('%d.%m.%Y')
    except TypeError("Не правильно ввели данные"):
        print("Не правильно ввели данные")
    else:
        return second_date


if __name__ == "__main__":

    print(mask_account_card("Мир 1596837868705199"))
    print(get_date("2024-03-11T02:26:18.671407"))
