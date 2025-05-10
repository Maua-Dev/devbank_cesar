from typing import Dict, Optional, List, Tuple
from src.app.entities.user import User
from src.app.entities.trasaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum

class User_repository:
    users: Dict[int, User]

    def __init__(self):
        self.users = {}

    def create_user(self, user: User) -> User:
        
        self.users[len(self.users.values) + 1] = user
        return user

    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id, None)
    
    def update_current_balance(self, user_id: int, value: float, transaction_type):
        user = self.get_user(user_id)
        if transaction_type == TransactionTypeEnum("DEPOSIT"):
            user.current_balance = user.current_balance + value
        if transaction_type == TransactionTypeEnum("WITHDRAW"):
            user.current_balance = user.current_balance - value
        