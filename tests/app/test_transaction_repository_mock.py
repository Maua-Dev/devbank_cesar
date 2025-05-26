from src.app.entities.trasaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repo.transaction_repository_mock import Trasaction_repository

# class Test_Trasaction_repositoryMock:
   
#     # def test_create_transaction(transaction):
#     #     repo = Trasaction_repository
#     #     transaction = Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, value = 200.0, timestamp = 212.0, current_balance = 1000.0)
#     #     repo.create_transaction(transaction = transaction)
#     #     history = repo.get_history()
#     #     assert history == {
#     #         1: Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, value = 200.0, timestamp = 123.0, current_balance = 1000.0),  
#     #         2: Transaction(transaction_type = TransactionTypeEnum.WITHDRAW, value = 100.0, timestamp = 321.0, current_balance = 1000.0),
#     #         3: Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, value = 200.0, timestamp = 212.0, current_balance = 1000.0) 
#     #         }
#     # def test_get_history(self):
#     #     repo = Trasaction_repository
#     #     history = repo.get_history()
#     #     assert history == {
#     #          1: Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, value = 200.0, timestamp = 123.0, current_balance = 1000.0),  
#     #          2: Transaction(transaction_type = TransactionTypeEnum.WITHDRAW, value = 100.0, timestamp = 321.0, current_balance = 1000.0),}