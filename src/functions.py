import json

def json_file_to_dict(filename):
    """Преобразует json file к словарю"""
    with open(filename) as file:
        return json.load(file)

def find_executed_transactions(list_of_all_transactions):
    """Принимает список словарей (список всех транзакций)
    Возвращает только исполненные транзакции"""
    list_of_executed_transactions = []
    for transaction in list_of_all_transactions:
        if transaction.get('state') == 'EXECUTED' and transaction.get('date'):
            list_of_executed_transactions.append(transaction)
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
        name_of_banc_card = []
        numbers_of_banc_card = ""
        for symbol in str_of_numbers:
            if symbol.isalpha():
                name_of_banc_card += symbol
            elif symbol.isdigit():
                numbers_of_banc_card += symbol

        numbers_formatted = (numbers_of_banc_card[0:4] + " "
                             + numbers_of_banc_card[4:6] + "** **** "
                             + numbers_of_banc_card[-4:])
        return (str_of_numbers[0: -16] + str_of_numbers[-16: -12] +
                " **** **" +str_of_numbers[-6:-4] + " " + str_of_numbers[-4:])