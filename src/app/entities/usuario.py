from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum
import re


class Usuario:
    name: str
    agency: str
    account: str
    current_balance: float


    def __init__(self, name: str=None, agency: str=None, account: str=None, current_balance: float=1000):
        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name

        validation_agency = self.validate_agency(agency)
        if validation_agency[0] is False:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency = agency

        validation_account = self.validate_account(account)
        if validation_account[0] is False:
            raise ParamNotValidated("account", validation_account[1])
        self.account = account

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance


    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Name is required")
        if type(name) != str:
            return (False, "Name must be a string")
        if len(name) < 3:
            return (False, "Name must be at least 3 characters long")
        return (True, "")
    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:
        if agency is None:
            return (False, "Agency is required")
        if type(agency) != str:
            return (False, "Agency must be a string")
        if len(agency) < 4 or len(agency) > 4:
            return (False, "Agency is a 4 character param")
        return (True, "")
    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:
        if account is None:
            return (False, "Agency is required")
        if type(account) != str:
            return (False, "Agency must be a string")
        if account !=  re.match("^([0-9]{5}\-[0-9]{1})$", account):
            return (False, "Agency must follow xxxxx-x format")
        return (True, "")
    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, float]:
        if type(current_balance) != float:
            return (False, "Current balance must be a number")
        if current_balance < 0:
            return(False, "Current balance must be a positive value")
        return (True, "")
    
def __eq__(self,other):
    return self.name == other.name and self.agency == other.agency and self.account == other.account and self.current_balance == other.current_balance
    
def __repr__(self):
    return f"Item(name={self.name}, agency={self.agency}, account={self.account}, current_balance={self.current_balance})"