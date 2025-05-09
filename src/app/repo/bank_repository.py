from typing import Dict, Optional, List, Tuple
from app.entities.usuario import Usuario
from app.entities.trasacao import Transacao

class Trasaction_repository:
    user: List[Usuario]
    transactions: Dict[int, Transacao]

    def __init__(self):
        self.transactions = {}

    def create_transaction(self, transaction: Transacao, transaction_id: int) -> Transacao:
        
        self.transactions[transaction_id] = transaction
        return transaction

    def deposit(self):
        Usuario.current_balance = Transacao.at_time_balance
        Usuario.current_balance + Transacao.value = Usuario.current_balance
        def create_transaction(self, transaction: Transacao, transaction_id: int) -> Transacao:
        
            self.transactions[transaction_id] = transaction
            return transaction


        



