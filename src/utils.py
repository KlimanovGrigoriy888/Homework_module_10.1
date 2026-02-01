import json
from json import JSONDecodeError
import os
from src.external_api import get_course_curensy

from tests.test_generators import transactions

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)),"data", "operations.json")

def get_transactions(path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as data_file:
        try:
            operations = json.load(data_file)
            return operations
        except JSONDecodeError:
            print("Ошибка декодирования файла")
            return []


def get_amount_transactions(transactions: list[dict]) -> float:
    """функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —
float. Если транзакция была в USD или EUR, происходит обращение к функции конвертации в модуле external_api для
получения текущего курса валют и конвертации суммы операции в рубли"""
    sum_dict_amount_transactions =[] # извлеченные данные из входных транзакций в виде списка [{'code': 'XXX', 'amount': 'XX.XX'}]
    for transaction in transactions:
        dict_amount_transactions = {}
        get_currency_transaction = transaction.get("operationAmount",{}).get("currency",{}).get("code")
        get_amount_transaction = transaction.get("operationAmount",{}).get("amount")
        dict_amount_transactions["code"] = get_currency_transaction
        dict_amount_transactions["amount"] = get_amount_transaction
        sum_dict_amount_transactions.append(dict_amount_transactions)
    print(sum_dict_amount_transactions)

    amount_rub = 0
    amount_convert = 0
    exchange_rate_currensy_for_rub = {'success': True, 'timestamp': 1769955604, 'base': 'RUB', 'date': '2026-02-01', 'rates': {'AED': 0.048084, 'AFN': 0.851057, 'ALL': 1.067705, 'AMD': 5.003313, 'ANG': 0.023438, 'AOA': 12.006385, 'ARS': 18.945732, 'AUD': 0.018844, 'AWG': 0.0236, 'AZN': 0.02231, 'BAM': 0.021602, 'BBD': 0.026582, 'BDT': 1.612768, 'BGN': 0.021988, 'BHD': 0.00496, 'BIF': 39.099845, 'BMD': 0.013093, 'BND': 0.016714, 'BOB': 0.091197, 'BRL': 0.068824, 'BSD': 0.013197, 'BTC': 1.55354e-07, 'BTN': 1.211951, 'BWP': 0.172686, 'BYN': 0.03759, 'BYR': 256.624917, 'BZD': 0.026543, 'CAD': 0.017837, 'CDF': 29.655894, 'CHF': 0.010066, 'CLF': 0.000287, 'CLP': 11.344267, 'CNY': 0.09102, 'CNH': 0.091113, 'COP': 48.048376, 'CRC': 6.535233, 'CUC': 0.013093, 'CUP': 0.346967, 'CVE': 1.21786, 'CZK': 0.268782, 'DJF': 2.350121, 'DKK': 0.08251, 'DOP': 0.830903, 'DZD': 1.706108, 'EGP': 0.617473, 'ERN': 0.196397, 'ETB': 2.050192, 'EUR': 0.011045, 'FJD': 0.028866, 'FKP': 0.009564, 'GBP': 0.009515, 'GEL': 0.035286, 'GGP': 0.009564, 'GHS': 0.144577, 'GIP': 0.009564, 'GMD': 0.955802, 'GNF': 115.805169, 'GTQ': 0.101226, 'GYD': 2.7611, 'HKD': 0.10227, 'HNL': 0.348343, 'HRK': 0.083245, 'HTG': 1.727192, 'HUF': 4.211927, 'IDR': 219.617247, 'ILS': 0.040463, 'IMP': 0.009564, 'INR': 1.200566, 'IQD': 17.289596, 'IRR': 551.547177, 'ISK': 1.601423, 'JEP': 0.009564, 'JMD': 2.068147, 'JOD': 0.009284, 'JPY': 2.026355, 'KES': 1.703888, 'KGS': 1.144997, 'KHR': 53.070466, 'KMF': 5.433644, 'KPW': 11.783797, 'KRW': 18.995531, 'KWD': 0.004019, 'KYD': 0.010998, 'KZT': 6.637619, 'LAK': 284.018114, 'LBP': 1181.846698, 'LKR': 4.0814, 'LRD': 2.378838, 'LSL': 0.209552, 'LTL': 0.038661, 'LVL': 0.00792, 'LYD': 0.082814, 'MAD': 0.119715, 'MDL': 0.221979, 'MGA': 58.979457, 'MKD': 0.680804, 'MMK': 27.499828, 'MNT': 46.695017, 'MOP': 0.10613, 'MRU': 0.526585, 'MUR': 0.594825, 'MVR': 0.202424, 'MWK': 22.884913, 'MXN': 0.228685, 'MYR': 0.051614, 'MZN': 0.834822, 'NAD': 0.209552, 'NGN': 18.153337, 'NIO': 0.485642, 'NOK': 0.126336, 'NPR': 1.939121, 'NZD': 0.021701, 'OMR': 0.005059, 'PAB': 0.013197, 'PEN': 0.044125, 'PGK': 0.056494, 'PHP': 0.771381, 'PKR': 3.692364, 'PLN': 0.046558, 'PYG': 88.402916, 'QAR': 0.048118, 'RON': 0.056299, 'RSD': 1.296664, 'RUB': 1, 'RWF': 19.255578, 'SAR': 0.049121, 'SBD': 0.105421, 'SCR': 0.190015, 'SDG': 7.875553, 'SEK': 0.116861, 'SGD': 0.016636, 'SHP': 0.009823, 'SLE': 0.31849, 'SLL': 274.555919, 'SOS': 7.542523, 'SRD': 0.498199, 'STD': 271.000901, 'STN': 0.270599, 'SVC': 0.115474, 'SYP': 144.804209, 'SZL': 0.209488, 'THB': 0.411171, 'TJS': 0.1232, 'TMT': 0.045826, 'TND': 0.037919, 'TOP': 0.031525, 'TRY': 0.56775, 'TTD': 0.089607, 'TWD': 0.413717, 'TZS': 33.983875, 'UAH': 0.565651, 'UGX': 47.183565, 'USD': 0.013093, 'UYU': 0.512149, 'UZS': 161.343053, 'VES': 4.529448, 'VND': 339.635222, 'VUV': 1.555349, 'WST': 0.035493, 'XAF': 7.244941, 'XAG': 0.000155, 'XAU': 2.693562e-06, 'XCD': 0.035385, 'XCG': 0.023785, 'XDR': 0.00901, 'XOF': 7.244941, 'XPF': 1.317208, 'YER': 3.120415, 'ZAR': 0.211347, 'ZMK': 117.853731, 'ZMW': 0.259002, 'ZWL': 4.215975}}#get_course_curensy() # список курсов валют из API
    for amount_transaction in sum_dict_amount_transactions: # Проведение операций сложения сумм операций с конвертацией.
        if amount_transaction.get("code") == 'RUB':
            amount_rub += float(amount_transaction.get("amount"))
        else: # Операция сложения если валюта не рубль.
            terget_code_curency = amount_transaction.get("code")
            target_amount_curency = amount_transaction.get("amount")
            target_exchange_rate_for_rub = exchange_rate_currensy_for_rub.get("rates").get(terget_code_curency)
            if target_exchange_rate_for_rub == None:
                continue
            target_convert_curency = float(target_amount_curency) * float(target_exchange_rate_for_rub)
            amount_convert += target_convert_curency

    full_amount_in_rub = round((amount_rub + amount_convert), 2)

    return full_amount_in_rub



if __name__ == "__main__":
    transactions = get_transactions(PATH_TO_FILE)
    print(get_amount_transactions(transactions))