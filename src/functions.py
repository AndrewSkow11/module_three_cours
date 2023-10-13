import json


def json_file_to_dict(filename):
    """Преобразует json file к словарю"""
    with open(filename) as file:
        return json.load(file)

def find_executed_transactions(number, list_of_all_transactions):
    """Возвращает список из заданного числа выполненных транзакций"""
    list_of_executed_transactions = []
    for transaction in list_of_all_transactions:
        if transaction['state'] == 'EXECUTED':
            list_of_executed_transactions.append(transaction)
            if len(list_of_executed_transactions) >= number:
                break
    return list_of_executed_transactions

def convert_date (str_of_date):
    """Конверитирует дату к виду 14.10.2018"""
    pass

# Пример вывода для одной операции:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.
