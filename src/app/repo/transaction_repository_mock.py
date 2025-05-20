from typing import Dict, Optional, List, Tuple
from src.app.entities.user import User
from src.app.entities.trasaction import Transaction

class Trasaction_repository:

    transactions: Dict[int, Transaction]

    def __init__(self):
        self.transactions = {}
    
    def create_transaction(self, transaction: Transaction):
        self.transactions[len(self.transactions.values) + 1] = transaction
        return transaction

    def get_history(self) -> List[Transaction]:
        return self.transactions.values()



        



