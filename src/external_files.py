import os
from typing import Any

import pandas as pd

PATH_TO_FILE_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transaction.csv")
PATH_TO_FILE_XLSX = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def read_csv(patch_to_file_csv: str) -> list[dict[Any, Any]]:
    """Принимает путь до .csv файла финансовых операций, возвращает список словарей с транзакциями."""
    if not patch_to_file_csv:
        return [dict()]
    csv_data_df = pd.read_csv(patch_to_file_csv, sep=';')
    result_list_of_dict = csv_data_df.to_dict(orient="records")
    return result_list_of_dict


def read_excel(patch_to_file_excel: str) -> list[dict[Any, Any]]:
    """Принимает путь до .xlsx файла финансовых операций, возвращает список словарей с транзакциями."""
    if not patch_to_file_excel:
        return [dict()]
    excel_data_df = pd.read_excel(patch_to_file_excel)
    result_list_of_dict = excel_data_df.to_dict(orient='records')
    return result_list_of_dict
