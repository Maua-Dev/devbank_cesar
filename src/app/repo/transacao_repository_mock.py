from typing import Dict, Optional, List, Tuple
from app.entities.usuario import Usuario
from app.entities.trasacao import Transacao

class Trasaction_repository:

    transactions: Dict[int, Transacao]

    def __init__(self):
        self.transactions = {}

    def deposit(self, transaction: Transacao, transaction_id: int):
        Usuario.current_balance = Transacao.at_time_balance
        Usuario.current_balance + Transacao.value = Usuario.current_balance
        self.transactions[transaction_id] = transaction
        Transacao.transaction_type = "Depósito"
        return transaction
    
    def withdraw(self, transaction: Transacao, transaction_id: int):
        Usuario.current_balance = Transacao.at_time_balance
        Usuario.current_balance - Transacao.value = Usuario.current_balance
        self.transactions[transaction_id] = transaction
        Transacao.transaction_type = "Saque"
        return transaction

    def get_history(self) -> List[Transacao]:
        return self.transactions.values()



        



