import pytest
from src.app.errors.entity_errors import ParamNotValidated
from src.app.entities.user import User

class Test_User:
    def test_user(self):
        user = User("test", "0000" ,"00000-0", 2000)
        assert user.name == "test"
        assert user.agency == "0000"
        assert user.current_balance == 2000