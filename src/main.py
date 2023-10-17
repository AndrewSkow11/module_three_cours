from src.functions import json_file_to_dict
from src.functions import find_executed_transactions
from src.functions import convert_date
from src.functions import convert_bank_numbers

# получаем полный список словарей
list_of_transaction = json_file_to_dict("operations.json")

# оставляем только выполненные транзакции
executed_transactions = find_executed_transactions(list_of_transaction)

# сортировка списка через лямбда-функцию
sorted_list_of_transactions = sorted(
    executed_transactions, key=lambda x: x['date'], reverse=True)

# Вывод согласно примеру из ТЗ:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.
for transaction in sorted_list_of_transactions[:5]:
    print(convert_date(transaction['date']), transaction['description'])

    if 'from' in transaction:
        print(convert_bank_numbers(transaction['from']) +
              " -> " + convert_bank_numbers(transaction['to']))
    else:
        print("... -> " + convert_bank_numbers(transaction['to']))

    print(transaction['operationAmount']['amount'],
          transaction['operationAmount']['currency']['name'])
    #  для пустой строчки после интерации
    print()
