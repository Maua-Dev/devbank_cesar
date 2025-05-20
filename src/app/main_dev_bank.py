from fastapi import FastAPI, HTTPException
from mangum import Mangum

from src.app.entities.trasaction import Transaction

from src.app.entities.user import User

from .errors.entity_errors import ParamNotValidated

from src.app.repo.user_repostory_mock import User_repository

from src.app.repo.transaction_repository_mock import Trasaction_repository

from src.app.enviroments_dev_bank import Environments

app = FastAPI()
user_repo = Environments.get_user_repo()
transaction_repo = Environments.get_transaction_repo()

in_use_id = 1

@app.get("/")
def get_user(user_id= in_use_id):

    user = user_repo.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")
    
    return user.to_dict()
