from src import functions

filename = "file_for_test.json"
variable_for_executed = functions.json_file_to_dict(filename)


def test_json_file_to_dict():
     assert type(functions.json_file_to_dict(filename)) is list
     assert type(functions.json_file_to_dict(filename)[0]) is dict

def test_find_executed_transactions():
     list_of_dict = functions.find_executed_transactions(variable_for_executed)
     assert type(list_of_dict) is list
     assert type(list_of_dict[0]) is dict
     assert list_of_dict[0]['sta']
def test_convert_data():
    assert functions.convert_date("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert functions.convert_date("2018-03-23T10:45:06.972075") == "23.03.2018"


def test_convert_bank_numbers():
    assert functions.convert_bank_numbers("Visa Classic 4195191172583802") == "Visa Classic 4195 **** **58 3802"

