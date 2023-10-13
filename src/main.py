from functions import *
import transaction

# получаем полный список словарей
list_of_transaction = json_file_to_dict("operations.json")

# получаем список из 5 транзакций
five_ex_transactions = find_executed_transactions(
    5, list_of_transaction)

# сортировка по дате в реверсивном порядке
sorted_five_ex_transactions = sorted(
    five_ex_transactions, key=lambda x: x['date'], reverse=True)

for transaction in sorted_five_ex_transactions:
    print(convert_date(transaction['date']), transaction['description'])

    if 'from' in transaction:
        print(convert_bank_numbers(transaction['from']) +
          " -> " + convert_bank_numbers(transaction['to']))
    else:
        print("... -> " + convert_bank_numbers(transaction['to']))


    print()
