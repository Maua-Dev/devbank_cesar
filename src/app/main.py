from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .repo.item_repository_mock import ItemRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.item_type_enum import ItemTypeEnum

from .entities.item import Item


app = FastAPI()

repo = Environments.get_item_repo()()

@app.get("/items/get_all_items")
def get_all_items():
    items = repo.get_all_items()
    return {
        "items": [item.to_dict() for item in items]
    }

@app.get("/items/{item_id}")
def get_item(item_id: int):
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo.get_item(item_id)
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not found")
    
    return {
        "item_id": item_id,
        "item": item.to_dict()    
    }

@app.post("/items/create_item", status_code=201)
def create_item(request: dict):
    item_id = request.get("item_id")
    
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo.get_item(item_id)
    if item is not None:
        raise HTTPException(status_code=409, detail="Item already exists")
    
    name = request.get("name")
    price = request.get("price")
    item_type = request.get("item_type")
    if item_type is None:
        raise HTTPException(status_code=400, detail="Item type is required")
    if type(item_type) != str:
        raise HTTPException(status_code=400, detail="Item type must be a string")
    if item_type not in [possible_type.value for possible_type in ItemTypeEnum]:
        raise HTTPException(status_code=400, detail="Item type is not a valid one")
    
    admin_permission = request.get("admin_permission")
    
    try:
        item = Item(name=name, price=price, item_type=ItemTypeEnum[item_type], admin_permission=admin_permission)
    except ParamNotValidated as err:
        raise HTTPException(status_code=400, detail=err.message)
    
    item_response = repo.create_item(item, item_id)
    return {
        "item_id": item_id,
        "item": item_response.to_dict()    
    }
    
@app.delete("/items/delete_item")
def delete_item(request: dict):
    item_id = request.get("item_id")
    
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo.get_item(item_id)
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not found")
    
    if item.admin_permission == True:
        raise HTTPException(status_code=403, detail="Item Not found")
    
    item_deleted = repo.delete_item(item_id)
    
    return {
        "item_id": item_id,
        "item": item_deleted.to_dict()    
    }
    
@app.put("/items/update_item")
def update_item(request: dict):
    item_id = request.get("item_id")
    
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo.get_item(item_id)
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not found")
    
    if item.admin_permission == True:
        raise HTTPException(status_code=403, detail="Item Not found")
    
    name = request.get("name")
    price = request.get("price")
    admin_permission = request.get("admin_permission")
    
    item_type_value = request.get("item_type")
    if item_type_value != None:
        if type(item_type_value) != str:
            raise HTTPException(status_code=400, detail="Item type must be a string")
        if item_type_value not in [possible_type.value for possible_type in ItemTypeEnum]:
            raise HTTPException(status_code=400, detail="Item type is not a valid one")
        item_type = ItemTypeEnum[item_type_value]
    else:
        item_type = None
        
    item_updated = repo.update_item(item_id, name, price, item_type, admin_permission)
    
    return {
        "item_id": item_id,
        "item": item_updated.to_dict()    
    }

# from fastapi import FastAPI, HTTPException
# from mangum import Mangum

# from .enviroments_dev_bank import Environments

# from .entities.trasaction import Transaction

# from .enums.transaction_type_enum import TransactionTypeEnum

# from time import time 

# app = FastAPI()
# user_repo = Environments.get_user_repo()()
# transaction_repo = Environments.get_transaction_repo()()

# in_use_id = 1

# @app.get("/")
# def get_user():
#     user = user_repo.get_user(in_use_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User Not found")
#     else:
#         return user.to_dict()

# @app.get("/history")
# def get_history():
#     history = transaction_repo.get_history()
#     if history is None:
#         return None
#     else:
#         return transaction_repo.transactions


# @app.post("/deposit")
# def deposit(request: dict):

#     dois = request.get("2")
#     cinco = request.get("5")
#     dez = request.get("10")
#     vinte = request.get("20")
#     cinquenta = request.get("50")
#     cem = request.get("100")
#     duzentos = request.get("200")

#     value = dois * 2 + cinco * 5 + dez * 10 + vinte * 20 + cinquenta * 50 + cem * 100 + duzentos * 200

#     if value is None:
#         return None
#     elif value <0:
#         raise HTTPException(status_code=400, detail="Deposited value must be positive")
#     elif value >= 2*user_repo.current_balance:
#         raise HTTPException(status_code=403, detail="Depósito suspeito")
#     else:
#         user_repo.update_current_balance(in_use_id,value,TransactionTypeEnum.DEPOSIT)
#         timestamp = time.time()
#         transaction = Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, value = float(value), current_balance = user_repo.current_balance, timestamp = float(timestamp))
#         transaction_repo.create_transaction(transaction)
#         return {
#             "current_balance": user_repo.current_balance,
#             "timestamp": timestamp
#         }
    
# @app.post("/withdraw")
# def withdraw(request: dict):

#     dois = request.get("2")
#     cinco = request.get("5")
#     dez = request.get("10")
#     vinte = request.get("20")
#     cinquenta = request.get("50")
#     cem = request.get("100")
#     duzentos = request.get("200")

#     value = dois * 2 + cinco * 5 + dez * 10 + vinte * 20 + cinquenta * 50 + cem * 100 + duzentos * 200

#     if value is None:
#         return None
#     elif value <0:
#         raise HTTPException(status_code=400, detail="Withdrawn value must be positive")
#     elif value > user_repo.current_balance:
#         raise HTTPException(status_code=403, detail="Saldo insuficiente para a transação")
#     else:
#         user_repo.update_current_balance(in_use_id,value,TransactionTypeEnum.WITHDRAW)
#         timestamp = time.time()
#         transaction = Transaction(transaction_type = TransactionTypeEnum.WITHDRAW, value = float(value), current_balance = user_repo.current_balance, timestamp = float(timestamp))
#         transaction_repo.create_transaction(transaction)
#         return {
#             "current_balance": user_repo.current_balance,
#             "timestamp": timestamp
#         }


handler = Mangum(app, lifespan="off")
