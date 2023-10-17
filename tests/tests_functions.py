import json
# import pytest
from src.functions import json_file_to_dict
from src.functions import find_executed_transactions
from src.functions import convert_date
from src.functions import convert_bank_numbers


def test_json_file_to_dict():
    """Преобразует json file к словарю"""
    assert type(json_file_to_dict("simply.json")) is list
    assert type(json_file_to_dict("simply.json")[0]) is dict
    assert json_file_to_dict("simply.json") == [{"id": 441945886}, {"id": 41428829}]


# def test_find_executed_transactions():
#     assert len(find_executed_transactions(list_of_transaction)) == 85

def test_convert_date():
    """Конверитирует 'date': '2019-08-26T10:50:58.294041' к виду 14.10.2018"""
    assert convert_date("2019-08-26T10:50:58.294041") == ("26.08.2019")

