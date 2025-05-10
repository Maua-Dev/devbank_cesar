from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum
import re


class Transacao:
    transaction_type: str
    value: float
    at_time_balance: float
    timestamp: float
    

    def __init__(self, transaction_type: str=None, value: float=None, at_time_balance: float=None, timestamp: float=None):
        validation_transaction_type = self.validate_transaction_type(transaction_type)
        if validation_transaction_type[0] is False:
            raise ParamNotValidated("transaction_type", validation_transaction_type[1])
        self.transaction_type = transaction_type

        validation_value = self.validate_value(value)
        if validation_value[0] is False:
            raise ParamNotValidated("value", validation_value[1])
        self.value = value
    
        validation_at_time_balance = self.validate_at_time_balance(at_time_balance)
        if validation_at_time_balance[0] is False:
            raise ParamNotValidated("at_time_balance", validation_at_time_balance[1])
        self.at_time_balance = at_time_balance

        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp


    @staticmethod
    def validate_transaction_type(transaction_type: str) -> Tuple[bool, str]:
        if transaction_type is None:
            return (False, "Transaction type is required")
        if type(transaction_type) != str:
            return (False, "Transaction type must be a string")
        if transaction_type != ("Saque") or transaction_type != ("Depósito"):
            return (False, "Transaction type must be a deposit or a withdraw")
        return (True, "")
    
    @staticmethod
    def validate_value(value: float) -> Tuple[bool, float]:
        if value is None:
            return None
        if type(value) != float:
            return (False, "Value must be a number")
        if value < 0:
            return(False, "Value must be a positive value")
        return (True, "")

    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool, float]:
        if type(timestamp) != float:
            return (False, "At time balance must be a number")
        if timestamp < 0:
            return(False, "At time balance must be a positive value")
        return (True, "")
    
    @staticmethod
    def validate_at__time_balance(at_time_balance: float) -> Tuple[bool, float]:
        if type(at_time_balance) != float:
            return (False, "At time balance must be a number")
        if at_time_balance < 0:
            return(False, "At time balance must be a positive value")
        return (True, "")

def __eq__(self,other):
    return self.transaction_type == other.transaction_type and self.value == other.value and self.timestamp == other.timestamp and self.at_time_balance == other.at_time_balance
    
def __repr__(self):
    return f"Transacao(transaction_type={self.transaction_type}, value={self.value}, timestamp={self.timestamp}, at_time_balance={self.at_time_balance})"