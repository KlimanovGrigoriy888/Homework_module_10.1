from unittest.mock import patch

import pytest

from src.external_api import get_course_currency


@pytest.mark.parametrize(
    "status_code, expected_result",
    [
        (401, (False, {})),
        (404, (False, {})),
        (429, (False, {})),
        (500, (False, {})),
    ],
)
@patch("requests.request")
def test_get_course_currency_bed_response(mosk_get, status_code, expected_result):
    mosk_get.return_value.status_code = status_code
    mosk_get.return_value.json.return_value = expected_result
    assert get_course_currency() == expected_result


@patch("requests.request")
def test_get_course_currency_success(mosk_get):

    mosk_get.return_value.status_code = 200
    mosk_get.return_value.json.return_value = []

    assert get_course_currency() == (True, [])
