import os
import requests
from dotenv import load_dotenv
from typing import Union

load_dotenv()
apikey = os.getenv("API_KEY")


def get_course_curensy() -> dict:
    url = "https://api.apilayer.com/exchangerates_data/latest?symbols=&base=RUB"

    payload = {}
    headers = {
        "apikey": apikey
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:
        return False, {}
    result = response.json()
    return result


if __name__ == "__main__":
    print(get_course_curensy())