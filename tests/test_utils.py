from code.utils import sort_by_date, change_date_format, masking_card, output_money, output_data
import pytest


@pytest.fixture()
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


def test_output_money():
    assert output_money({"amount": "67314.70", "currency": {"name": "руб."}}) == "67314.70 руб."
    assert output_money({"amount": "67314.70", "currency": {"name": "USD"}}) == "67314.70 USD"
    assert output_money({"amount": "", "currency": {"name": ""}}) == " "


def test_output_data():
    data = {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }
    result = "12.09.2018 Перевод организации\nVisa Platinum 1246 37** **** 3588 -> Счет **1657\n67314.70 руб.\n"
    assert output_data(data) == result
