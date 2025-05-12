import pytest
from src.app.errors.entity_errors import ParamNotValidated
from src.app.entities.user import User

class Test_User:
    def test_user(self):
        user = User("test", "0000" ,"00000-0", 2000)
        assert user.name == "test"
        assert user.agency == "0000"
        assert user.account == "00000-0"
        assert user.current_balance == 2000

    def test_user_dict(self):
        user = User("test", "0000", "00000-0", 2000)
        assert user.to_dict() == {'agency': '0000', 'account': '00000-0', 'name': 'test', 'current_balance': 2000}

    def test_user_name_is_none(self):
        with pytest.raises(ParamNotValidated):       
            User( agency = "0000", account = "00000-0", current_balance = 2000)

    def test_user_name_has_less_than_3_characters(self):
        with pytest.raises(ParamNotValidated):       
            User( name = 'te', agency = "0000", account = "00000-0", current_balance = 2000)

    def test_user_name_is_not_str(self):
        with pytest.raises(ParamNotValidated):       
            User( name = 1, agency = "0000", account = "00000-0", current_balance = 2000)

    def test_user_agency_is_none(self):
        with pytest.raises(ParamNotValidated):       
            User( name = 'test', account = "00000-0", current_balance = 2000)

    def test_user_agency_is_less_than_4(self):
        with pytest.raises(ParamNotValidated):       
            User( name = 'test', agency = "000", account = "00000-0", current_balance = 2000)

    def test_user_agency_is_more_than_4(self):
        with pytest.raises(ParamNotValidated):       
            User( name = 'test', agency = "00000", account = "00000-0", current_balance = 2000)

    def test_user_agency_is_not_str(self):
        with pytest.raises(ParamNotValidated):       
            User( name = 'test', agency = 1, account = "00000-0", current_balance = 2000)

    def test_user_account_none(self):
        with pytest.raises(ParamNotValidated):       
            User( name = 'test', agency = "0000", current_balance = 2000)

    def test_user_account_has_no_hifen(self):
        with pytest.raises(ParamNotValidated):       
            User( name = 'test', agency = "0000", account = "000000", current_balance = 2000)

    def test_user_account_has_less_than_6_characters(self):
        with pytest.raises(ParamNotValidated):       
            User( name = 'test', agency = "0000", account = "0000-0", current_balance = 2000)

    def test_user_account_has_more_than_6_characters(self):
        with pytest.raises(ParamNotValidated):       
            User( name = 'test', agency = "0000", account = "000000-0", current_balance = 2000)

    def test_user_account_not_str(self):
        with pytest.raises(ParamNotValidated):       
            User( name = 'test', agency = "0000", account = 1, current_balance = 2000)

    def test_user_current_balance_not_float(self):
        with pytest.raises(ParamNotValidated):       
            User( name = 'test', agency = "0000", account = '00000-0', current_balance = '0')

    def test_user_current_balance_less_than_0(self):
        with pytest.raises(ParamNotValidated):       
            User( name = 'test', agency = "0000", account = '00000-0', current_balance = -2000)
    
