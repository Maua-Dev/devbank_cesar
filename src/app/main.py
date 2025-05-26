from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .enviroments_dev_bank import Environments

from .entities.trasaction import Transaction

from .enums.transaction_type_enum import TransactionTypeEnum

from time import time 

app = FastAPI()
user_repo = Environments.get_user_repo()()
transaction_repo = Environments.get_transaction_repo()()

in_use_id = 1

@app.get("/")
def get_user():
    user = user_repo.get_user(in_use_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")
    else:
        return user.to_dict()

@app.get("/history")
def get_history():
    history = transaction_repo.get_history()
    return {
        "all_transactions": [transaction.to_dict() for transaction in history]
    }

@app.post("/deposit")
def deposit(request: dict):

    dois = request.get("2")
    cinco = request.get("5")
    dez = request.get("10")
    vinte = request.get("20")
    cinquenta = request.get("50")
    cem = request.get("100")
    duzentos = request.get("200")

    value = dois * 2 + cinco * 5 + dez * 10 + vinte * 20 + cinquenta * 50 + cem * 100 + duzentos * 200
    user = user_repo.get_user(in_use_id)

    if value is None:
        return None
    elif value <0:
        raise HTTPException(status_code=400, detail="Deposited value must be positive")
    elif value >= 2*user.current_balance:
        raise HTTPException(status_code=403, detail="Depósito suspeito")
    else:
        current_user_balance = user_repo.update_current_balance(in_use_id,value,TransactionTypeEnum.DEPOSIT)
        timestamp = time()
        transaction = Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, value = float(value), current_balance = float(current_user_balance), timestamp = float(timestamp))
        transaction_repo.create_transaction(transaction)
        return {
            "current_balance": current_user_balance,
            "timestamp": timestamp
        }
    
@app.post("/withdraw")
def withdraw(request: dict):

    dois = request.get("2")
    cinco = request.get("5")
    dez = request.get("10")
    vinte = request.get("20")
    cinquenta = request.get("50")
    cem = request.get("100")
    duzentos = request.get("200")

    value = dois * 2 + cinco * 5 + dez * 10 + vinte * 20 + cinquenta * 50 + cem * 100 + duzentos * 200
    user = user_repo.get_user(in_use_id)

    if value is None:
        return None
    elif value <0:
        raise HTTPException(status_code=400, detail="Withdrawn value must be positive")
    elif value > user.current_balance:
        raise HTTPException(status_code=403, detail="Saldo insuficiente para a transação")
    else:
        current_user_balance = user_repo.update_current_balance(in_use_id,value,TransactionTypeEnum.WITHDRAW)
        timestamp = time()
        transaction = Transaction(transaction_type = TransactionTypeEnum.WITHDRAW, value = float(value), current_balance = float(current_user_balance), timestamp = float(timestamp))
        transaction_repo.create_transaction(transaction)
        return {
            "current_balance": current_user_balance,
            "timestamp": timestamp
        }


handler = Mangum(app, lifespan="off")
