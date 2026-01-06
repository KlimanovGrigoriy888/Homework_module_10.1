import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def my_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.mark.parametrize("state_select, expected_result",
                         [('EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                          ('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
                          ])
def test_filter_by_state(my_list, state_select, expected_result):
    assert filter_by_state(my_list, state_select=state_select) == expected_result


def test_filter_by_state_not_state_select(my_list):
    assert filter_by_state(my_list, ) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.mark.parametrize("state_select, expected_result",
                         [('NOT_SELECT', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                          {'id': 939719570, 'state': 'EXECUTED',
                                           'date': '2018-06-30T02:08:58.425572'}]),
                          ('1234fff', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])])
def test_filter_by_state_wrong_state_select(my_list, state_select, expected_result):
    assert filter_by_state(my_list, ) == expected_result


def test_filter_by_state_not_my_list():
    with pytest.raises(TypeError):
        filter_by_state()


@pytest.mark.parametrize("key_sort, expected_result",
                         [(True, [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                          (False, [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                   {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])
                          ])
def test_sort_by_date(my_list, key_sort, expected_result):
    assert sort_by_date(my_list, key_sort) == expected_result


@pytest.fixture
def my_list_same_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:21:33.419441'}]


@pytest.mark.parametrize("key_sort, expected_result",
                         [(True, [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                  {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:27:25.241689'},
                                  {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:21:33.419441'},
                                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:08:58.425572'}]),
                          (False, [{'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:08:58.425572'},
                                   {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:21:33.419441'},
                                   {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:27:25.241689'},
                                   {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])
                          ])
def test_sort_by_date_same_date(my_list_same_date, key_sort, expected_result):
    assert sort_by_date(my_list_same_date, key_sort) == expected_result


@pytest.fixture
def my_list_incorrect_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2023-04-07 14:23:01'},
            {'id': 594226727, 'state': 'CANCELED', 'date': 'April 07, 2023'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': 'Fri Apr  7 14:23:01 2023'}]


def test_sort_by_date_wrong_date(my_list_incorrect_date):
    with pytest.raises(ValueError):
        sort_by_date(my_list_incorrect_date)
