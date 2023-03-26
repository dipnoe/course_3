from code.utils import sort_by_date, change_date_format, masking_card, output_money
import pytest


@pytest.fixture
def collection():
    return [
        {},
        {"state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041"},
        {"state": "EXECUTED",
         "date": "2018"},
        {"state": "CANCELED",
         "date": "2019-08-26T10:50:58.294041"},
        {"st": "EXECUTED",
         "date": "2018-01-26T10:50:58.294041"},
        {"state": "EXECUTED",
         "date": "2018-01-26T10:50:58.294041"},
        {"state": "EXECUTED",
         "dt": "2018-01-26T10:50:58.294041"},
        {"EXECUTED": "state",
         "2018-01-26T10:50:58.294041": "date"}
    ]


def test_sort_by_data(collection):
    assert sort_by_date(collection) == [
        {"state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041"},
        {"state": "EXECUTED",
         "date": "2018-01-26T10:50:58.294041"},
        {"state": "EXECUTED",
         "date": "2018"}
    ]


def test_change_date_format():
    assert change_date_format("2018-09-12T21:27:25.241689") == "12.09.2018"
    assert change_date_format("2018-09-12") == "12.09.2018"
    assert change_date_format("") == ""
    assert change_date_format("12.09.2018") == "12.09.2018"


def test_masking_card():
    assert masking_card("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"
    assert masking_card("Счет 14211924144426031657") == "Счет **1657"
    assert masking_card('') == ''
    assert masking_card('1 2 3') == 'Uncorrected card_info'

