import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("API_KEY")


def get_course_currency() -> tuple[bool, Any]:
    """Функция обращается к внешнему API для получения текущего курса валют по отношению к рублю"""
    url = "https://api.apilayer.com/exchangerates_data/latest?symbols=&base=RUB"

    payload = {}
    headers = {"apikey": apikey}

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.status_code)
    result = response.json()
    if response.status_code == 200:
        return True, result
    elif response.status_code == 401:
        print("No valid API key provided.")
        return False, {}
    elif response.status_code == 404:
        print("The requested resource doesn't exist.")
        return False, {}
    elif response.status_code == 429:
        print("API request limit exceeded. See section Rate Limiting for more info.")
        return False, {}
    elif response.status_code >= 500:
        print("We have failed to process your request. (You can contact us anytime)")
        return False, {}
    else:
        return False, {}


if __name__ == "__main__":
    print(get_course_currency())
