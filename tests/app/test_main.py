from fastapi.exceptions import HTTPException
import pytest
from src.app.entities.trasaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.main import get_user, get_history, deposit, withdraw
from src.app.repo.transaction_repository_mock import Trasaction_repository
from src.app.entities.user import User
from src.app.repo.user_repostory_mock import User_repository        

# class Test_Main:

#     def test_get_user(id):
#         repo = User_repository
#         id = 1
#         response = get_user(id)
#         assert response == repo.get_user(1)

#     def test_get_history():
#         repo = Trasaction_repository
#         response = get_history()
#         assert response == repo.get_history()

#     def test_deposit():
#         repo = User_repository
#         response = {
#         "2": 1,
#         "5": 0,
#         "10": 0,
#         "20": 0,
#         "50": 0,
#         "100": 0,
#         "200": 0
#         }
#         deposito = deposit(response)
#         assert deposito == repo.update_current_balance(user_id = 1,value = 2, transaction_type = TransactionTypeEnum.DEPOSIT)

#     def test_withdraw():
#         repo = User_repository
#         response = {
#         "2": 1,
#         "5": 0,
#         "10": 0,
#         "20": 0,
#         "50": 0,
#         "100": 0,
#         "200": 0
#         }
#         deposito = withdraw(response)
#         assert deposito == repo.update_current_balance(user_id = 1,value = 2, transaction_type = TransactionTypeEnum.WITHDRAW)


"""quando vcs forem me passar o feedback, vcs podem me explicar o erros desses testes?? Eu n entendi bem pq ele n aceita as funções que eu coloquei e queria saber o motivo. Mt obrigado pela ajuda e pelo projeto. Boa correção :)"""