import pytest
from src.app.errors.entity_errors import ParamNotValidated
from src.app.entities.trasaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum

class Test_Transaction:
    def test_transaction(self):
        user = Transaction(TransactionTypeEnum.DEPOSIT, 1 , 1, 2000)
        assert user.transaction_type == TransactionTypeEnum.DEPOSIT
        assert user.value == 1
        assert user.timestamp == 1
        assert user.current_balance == 2000

    def test_transaction_dict(self):
        transaction = Transaction(TransactionTypeEnum.DEPOSIT, 1, 1, 2000)
        assert transaction.to_dict() == {'value': 1, 'timestamp': 1, 'transaction_type': TransactionTypeEnum.DEPOSIT, 'current_balance': 2000}

    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value = 1, timestamp = 1, current_balance = 2000)

    def test_transaction_type_is_not_enum(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type = 1, value = 1, timestamp = 1, current_balance = 2000)

    def test_transaction_type_is_not_enum(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type = 1, value = 1, timestamp = 1, current_balance = 2000)

    def test_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, timestamp = 1, current_balance = 2000)
    
    def test_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, value = 1, timestamp = 1, current_balance = 2000)

    def test_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, value = '0', timestamp = 1, current_balance = 2000)

    def test_value_is_less_than_0(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, value = -1, timestamp = 1, current_balance = 2000)

    def test_timestamp_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, timestamp = '0', value = 1, current_balance = 2000)

    def test_timestamp_is_less_less_than_0(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, timestamp = -1, value = 1, current_balance = 2000)

    def test_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, timestamp = 1, value = 1, current_balance = '0')

    def test_current_balance_is_less_than_0(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type = TransactionTypeEnum.DEPOSIT, timestamp = 1, value = 1, current_balance = -1)