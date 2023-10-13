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


def convert_date(str_of_date):
    """Конверитирует 'date': '2019-08-26T10:50:58.294041' к виду 14.10.2018"""
    year_month_day = str_of_date.split('T')[0].split('-')
    year = year_month_day[0]
    month = year_month_day[1]
    day = year_month_day[2]

    return f'{day}.{month}.{year}'

def convert_bank_numbers(str_of_numbers):
    """Функция принимает строку,
    если банковская карта - отображение Visa Platinum 7000 79** **** 6361,
    если счёт - Счет **9638"""
    if "Счет" in str_of_numbers:
        #Обработчка как счёта
        new_form_numbers = str_of_numbers[-4:]
        return "Счет " + "**" + (new_form_numbers)
    else:
        return "обработать как карту"

print(convert_bank_numbers("Счет 48894435694657014368"))
#print(convert_bank_numbers("Visa Gold 5999414228426353"))




# Пример вывода для одной операции:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.
