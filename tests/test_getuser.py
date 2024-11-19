import uuid

import pytest

from conftest import load_user_data
from utils.apis import APIS

@pytest.fixture(scope="module")
def apis():
    return  APIS()

def test_getuser_validation(apis):
    response = apis.get('users')
    print(response.json())
    assert response.status_code==200
    assert len(response.json())>0

def test_create_user_validation(apis):
    data_user = {
        "name": "teja",
        "username": "123",
        "email":"emo"
    }
    response = apis.post('users',data_user)
    print(response.json())
    assert response.status_code==201
    assert response.json()['name']=='teja'
    id=response.json()['id']
    responseget = apis.get('users/10')
    print(responseget.json())
    assert responseget.status_code == 200
    assert responseget.json()['name']=='Clementina DuBuque'


def test_update_users(apis,load_user_data):
    '''data_user = {
        "name": "teja Bhavani",
        "username": "123",
        "email":"emo"
    }'''
    data_user =load_user_data["new_user"]
    unique_email= f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    data_user["email"]=unique_email
    response = apis.put("users/1",data_user)
    print(response.json())
    assert response.status_code==200
    assert response.json()['name']=='teja Bhavani'


def test_delete_users(apis):
    response = apis.delete("users/1")
    print(response.json())
    assert response.status_code==200