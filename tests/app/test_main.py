from fastapi.exceptions import HTTPException
import pytest

from src.app.main import deposit
from src.app.repo.transaction_repository_mock import Trasaction_repository


# class Test_Main:
#     def test_deposit(self):
#         repo = Trasaction_repository()
#         request = {
#         "2": 1,
#         "5": 2,
#         "10": 3,
#         "20": 4,
#         "50": 5 ,
#         "100": 6,
#         "200": 0
#         }
#         response = deposit(request)
#         assert response['current_balance'] == 1972.0
#         assert type(response['timestamp']) == float
        
        
#     def test_get_item(self):
#         repo = ItemRepositoryMock()
#         item_id = 1
#         response = get_item(item_id=item_id)
#         assert response == {
#             'item_id' : item_id,
#             'item': repo.items.get(item_id).to_dict()
#         }
        
#     def test_get_item_id_is_none(self):
        
#         item_id = None
#         with pytest.raises(HTTPException) as err:
#             get_item(item_id=item_id)
    
#     def test_get_item_id_is_not_int(self):
#         item_id = '1'
#         with pytest.raises(HTTPException) as err:
#             get_item(item_id=item_id)
            
#     def test_get_item_id_is_not_positive(self):
#         item_id = -1
#         with pytest.raises(HTTPException) as err:
#             get_item(item_id=item_id)
            
#     def test_create_item(self):
#         repo = ItemRepositoryMock()
        
#         body = {
#             'item_id': 0,
#             'name': 'test',
#             'price': 1.0,
#             'item_type': 'TOY',
#             'admin_permission': False
#         }
#         response = create_item(request=body)
#         assert response == {'item_id': 0,'item': {'admin_permission': False, 'item_type': 'TOY', 'name': 'test', 'price': 1.0}}
    
#     def test_create_item_conflict(self):
#         repo = ItemRepositoryMock()
        
#         body = {
#             'item_id': 1,
#             'name': 'test',
#             'price': 1.0,
#             'item_type': 'TOY',
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
    
#     def test_create_item_missing_id(self):
#         body = {
#             'name': 'test',
#             'price': 1.0,
#             'item_type': 'TOY',
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
        
#     def test_create_item_id_is_not_int(self):
#         body = {
#             'item_id': '0',
#             'name': 'test',
#             'price': 1.0,
#             'item_type': 'TOY',
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
    
#     def test_create_item_id_is_not_positive(self):
#         body = {
#             'item_id': -1,
#             'name': 'test',
#             'price': 1.0,
#             'item_type': 'TOY',
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
            
#     def test_create_item_missing_type(self):
#         body = {
#             'item_id': 1,
#             'name': 'test',
#             'price': 1.0,
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
            
#     def test_create_item_item_type_is_not_string(self):
#         body = {
#             'item_id': 1,
#             'name': 'test',
#             'price': 1.0,
#             'item_type': 1,
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
            
#     def test_create_item_item_type_is_not_valid(self):
#         body = {
#             'item_id': 1,
#             'name': 'test',
#             'price': 1.0,
#             'item_type': 'test',
#             'admin_permission': False
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
            
#     def test_create_item_param_not_validated(self):
#         body = {
#             'item_id': 1,
#             'name': '',
#             'price': 1.0,
#             'item_type': 'TOY',
#             'admin_permission': False,
#         }
#         with pytest.raises(HTTPException) as err:
#             create_item(request=body)
            
#     def test_delete_item(self):
#         body = {
#             "item_id": 1
#         }
#         response = delete_item(request=body)
#         assert response == {'item_id': 1, 'item': {'name': 'Barbie', 'price': 48.9, 'item_type': 'TOY', 'admin_permission': False}}
        
#     def test_delete_item_missing_id(self):
#         with pytest.raises(HTTPException) as err:
#             delete_item(request={})
            
#     def test_delete_item_id_is_not_int(self):
#         body = {
#             "item_id": '1'
#         }
#         with pytest.raises(HTTPException) as err:
#             delete_item(request=body)
            
#     def test_delete_item_id_not_found(self):
#         body = {
#             "item_id": 100
#         }
#         with pytest.raises(HTTPException) as err:
#             delete_item(request=body)
            
#     def test_delete_item_id_not_positive(self):
#         body = {
#             "item_id": -100
#         }
#         with pytest.raises(HTTPException) as err:
#             delete_item(request=body)
            
#     def test_delete_item_without_admin_permission(self):
#         body = {
#             "item_id": 4
#         }
#         with pytest.raises(HTTPException) as err:
#             delete_item(request=body)
            
#     def test_update_item(self):
#         body = {
#             "item_id": 2,
#             "name": "test",
#             "price": 1.0,
#             "item_type": "TOY",
#             "admin_permission": False
#         }
#         response = update_item(request=body)
#         assert response == {'item_id': 2, 'item': {'name': 'test', 'price': 1.0, 'item_type': 'TOY', 'admin_permission': False}}
        
#     def test_update_item_missing_id(self):
#         body = {
#             "name": "test",
#             "price": 1.0,
#             "item_type": "TOY",
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
    
#     def test_update_item_id_is_not_int(self):
#         body = {
#             "item_id": "1",
#             "name": "test",
#             "price": 1.0,
#             "item_type": "TOY",
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
            
#     def test_update_item_not_positive(self):
#         body = {
#             "item_id": -1,
#             "name": "test",
#             "price": 1.0,
#             "item_type": "test",
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
            
#     def test_update_item_not_found(self):
#         body = {
#             "item_id": 1,
#             "name": "test",
#             "price": 1.0,
#             "item_type": "test",
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
            
#     def test_update_item_without_admin_permission(self):
#         body = {
#             "item_id": 4,
#             "name": "test",
#             "price": 1.0,
#             "item_type": "TOY",
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
    
#     def test_update_item_type_not_string(self):
#         body = {
#             "item_id": 1,
#             "name": "test",
#             "price": 1.0,
#             "item_type": 1,
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
            
#     def test_update_item_type_not_valid(self):
        
#         body = {
#             "item_id": 1,
#             "name": "test",
#             "price": 1.0,
#             "item_type": "test",
#             "admin_permission": False
#         }
#         with pytest.raises(HTTPException) as err:
#             update_item(request=body)
            