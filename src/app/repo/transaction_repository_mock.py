from typing import Dict, Optional, List, Tuple
from ..entities.user import User
from ..entities.trasaction import Transaction
from ..enums.transaction_type_enum import TransactionTypeEnum

class Trasaction_repository:
    all_transactions: Dict[int, Transaction]

    def __init__(self):
        self.all_transactions = {
            1: Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, value = 200.0, timestamp = 123.0, current_balance = 1000.0),  
            2: Transaction(transaction_type = TransactionTypeEnum.WITHDRAW, value = 100.0, timestamp = 321.0, current_balance = 1000.0),
            }


    def create_transaction(self, transaction: Transaction):
        self.all_transactions[len(self.all_transactions.values()) + 1] = transaction
        return transaction

    def get_history(self) -> List[Transaction]:
        return self.all_transactions.values()