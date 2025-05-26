from typing import Dict, Optional, List, Tuple
from ..entities.user import User
from ..entities.trasaction import Transaction
from ..enums.transaction_type_enum import TransactionTypeEnum

class User_repository:
    users: Dict[int, User]

    def __init__(self):
        self.users = {
            1: User(name="Vitor Soller", agency="0000", account="00000-0", current_balance=1000.0)
        }

    def create_user(self, user: User) -> User:
        
        self.users[len(self.users.values) + 1] = user
        return user

    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id, None)
    
    def update_current_balance(self, user_id: int, value: float, transaction_type):
        user = self.get_user(user_id)
        if transaction_type == TransactionTypeEnum("deposit"):
            user.current_balance = user.current_balance + value
        if transaction_type == TransactionTypeEnum("withdraw"):
            user.current_balance = user.current_balance - value
        return user.current_balance