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
    df_csv_data_replace_none = csv_data_df.astype(object).where(pd.notnull(csv_data_df), "")
    result_list_of_dict = df_csv_data_replace_none.to_dict(orient="records")
    return result_list_of_dict


def read_excel(patch_to_file_excel: str) -> list[dict[Any, Any]]:
    """Принимает путь до .xlsx файла финансовых операций, возвращает список словарей с транзакциями."""
    if not patch_to_file_excel:
        return [dict()]
    excel_data_df = pd.read_excel(patch_to_file_excel)
    df_excel_data_replace_none = excel_data_df.astype(object).where(pd.notnull(excel_data_df), "")
    result_list_of_dict = df_excel_data_replace_none.to_dict(orient='records')
    return result_list_of_dict


if __name__ == "__main__":
    result_1 = read_csv(PATH_TO_FILE_CSV)
    print(result_1)
    print(type(result_1))
    result_2 = read_excel(PATH_TO_FILE_XLSX)
    print(result_2)
    print(type(result_2))
