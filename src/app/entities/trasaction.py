from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.transaction_type_enum import TransactionTypeEnum
import re


class Transaction:
    transaction_type: TransactionTypeEnum
    value: float
    current_balance: float
    timestamp: float
    

    def __init__(self, transaction_type: TransactionTypeEnum=None, value: float=None, current_balance: float=None, timestamp: float=0):
        validation_transaction_type = self.validate_transaction_type(transaction_type)
        if validation_transaction_type[0] is False:
            raise ParamNotValidated("transaction_type", validation_transaction_type[1])
        self.transaction_type = transaction_type

        validation_value = self.validate_value(value)
        if validation_value[0] is False:
            raise ParamNotValidated("value", validation_value[1])
        self.value = value
    
        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", current_balance[1])
        self.current_balance = current_balance

        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp


    @staticmethod
    def validate_transaction_type(transaction_type: str) -> Tuple[bool, str]:
        if transaction_type is None:
            return (False, "Transaction type is required")
        if type(transaction_type) != TransactionTypeEnum:
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
    def validate_current_balance(current_balance: float) -> Tuple[bool, float]:
        if type(current_balance) != float:
            return (False, "Current balance must be a number")
        if current_balance < 0:
            return(False, "Current balance must be a positive value")
        return (True, "")

    def to_dict(self):
        return {
            "type": self.transaction_type,
            "value": self.value,
            "timestamp": self.timestamp,
            "current_balance": self.current_balance
        }

    def __eq__(self,other):
        return self.transaction_type == other.transaction_type and self.value == other.value and self.timestamp == other.timestamp and self.current_balance == other.current_balance
    
    def __repr__(self):
        return f"Transaction(type={self.transaction_type}, value={self.value}, timestamp={self.timestamp}, current_balance={self.current_balance})"