# По каждой операции есть следующие данные:
#
# id — id транзакциии
# date — информация о дате совершения операции
# state — статус перевода:
# EXECUTED — выполнена,
# CANCELED — отменена.
# operationAmount — сумма операции и валюта
# description — описание типа перевода
# from — откуда (может отсутстовать)
# to — куда


class Transaction:
    """Класс соедерижит все поля о транзацкции"""
    def __init__(self,
                 id, date, state, executed, canceled, operation_amount,
                 description, from_, to):
        self.id = id
        self.date = date
        self.state = state
        self.executed = executed
        self.canceled = canceled
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = from_
        self.to = to




