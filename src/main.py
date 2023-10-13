from functions import *
import transaction

# получаем полный список словарей
list_of_transaction = json_file_to_dict("operations.json")

# получаем список из 5 транзакций
five_ex_transactions = find_executed_transactions(
    5, list_of_transaction)





# print(obj['date'], obj['description'])
# print(f"{obj['from']} -> {obj['to']}")
# print(obj['operationAmount']['amount'],
#       obj['operationAmount']['currency']['name'])
# transaction1 = transaction.Transaction(obj["id"])
