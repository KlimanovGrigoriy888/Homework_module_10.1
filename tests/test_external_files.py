import pytest
import pandas as pd
from unittest.mock import patch

from src.external_files import read_csv, read_excel


def test_read_csv_valid_data():
    # Данные, которые должен вернуть read_csv
    mock_df = pd.DataFrame(
        {
            "id": [650703.0, 3598919.0],
            "state": ["EXECUTED", "EXECUTED"],
            "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
            "amount": [16210.0, 29740.0],
            "currency_name": ["Sol", "Peso"],
            "currency_code": ["PEN", "COP"],
            "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
            "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
            "description": ["Перевод организации", "Перевод с карты на карту"],
        }
    )

    # Ожидаемый результат преобразования to_dict
    expected_df = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]

    # Патчим функцию преобразования в DataFrame, где находится тестируемая функция
    with patch("src.external_files.pd.read_csv") as mock_read:
        # Функции pd.read_csv присваиваем результат как mock_df
        mock_read.return_value = mock_df
        # Даем функции несуществующий путь к файлу
        result = read_csv("path.csv")
        # Проверка
        assert result == expected_df
        mock_read.assert_called_once_with("path.csv", sep=";")


def test_read_csv_empty_df():
    # Проверка не пустой DataFrame
    with patch("src.external_files.pd.read_csv") as mock_read:
        mock_read.return_value = pd.DataFrame()
        result = read_csv("")
        assert result == [{}]


def test_read_csv_file_not_found():
    # Проверка не существующего пути к файлу
    with pytest.raises(FileNotFoundError):
        read_csv("non_existent_file.csv")


def test_read_excel_valid_data():
    # Данные, которые должен вернуть read_csv
    mock_df = pd.DataFrame(
        {
            "id": [650703.0, 3598919.0],
            "state": ["EXECUTED", "EXECUTED"],
            "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
            "amount": [16210.0, 29740.0],
            "currency_name": ["Sol", "Peso"],
            "currency_code": ["PEN", "COP"],
            "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
            "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
            "description": ["Перевод организации", "Перевод с карты на карту"],
        }
    )

    # Ожидаемый результат преобразования to_dict
    expected_df = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]

    # Патчим функцию преобразования в DataFrame, где находится тестируемая функция
    with patch("src.external_files.pd.read_excel") as mock_read:
        # Функции pd.read_csv присваиваем результат как mock_df
        mock_read.return_value = mock_df
        # Даем функции несуществующий путь к файлу
        result = read_excel("path.csv")
        # Проверка
        assert result == expected_df
        mock_read.assert_called_once_with("path.csv")


def test_read_excel_empty_df():
    # Проверка не пустой DataFrame
    with patch("src.external_files.pd.read_excel") as mock_read:
        mock_read.return_value = pd.DataFrame()
        result = read_excel("")
        assert result == [{}]


def test_read_excel_file_not_found():
    # Проверка не существующего пути к файлу
    with pytest.raises(FileNotFoundError):
        read_excel("non_existent_file.csv")
