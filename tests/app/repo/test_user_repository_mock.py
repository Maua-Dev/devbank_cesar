from src.app.entities.user import User
from src.app.repo.user_repostory_mock import User_repository
import pytest
from src.app.enums.transaction_type_enum import TransactionTypeEnum

class User_repository_test:

    def test_get_user(id):
        id = 1
        repo = User_repository
        user = repo.get_user(id)
        assert user == User(name="Vitor Soller", agency="0000", account="00000-0", current_balance=1000.0)

    def test_update_current_balance_deposit(id, transaction_type, value):
        id = 1
        transaction_type = TransactionTypeEnum.DEPOSIT
        repo = User_repository
        value = 200.0
        current_balance = repo.update_current_balance(id= id, value=value, transaction_type= transaction_type)
        assert current_balance == 1200.0

    def test_update_current_balance_withdraw(id, transaction_type, value):
        id = 1
        transaction_type = TransactionTypeEnum.WITHDRAW
        repo = User_repository
        value = 200.0
        current_balance = repo.update_current_balance(id= id, value=value, transaction_type= transaction_type)
        assert current_balance == 800.0
    # def test_update_current_balance(id, transaction_type, value):
