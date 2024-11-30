import pytest
import requests
from data import Url
from methods.create_user import CreateUser
from methods.authorization_user import AuthorizationUser
from methods.update_user_data import UpdateUserData
from methods.create_order import CreateOrder
from methods.get_orders_specific_user import GetOrdersSpecificUser


@pytest.fixture()
def user():
    return CreateUser()


@pytest.fixture()
def real_user():
    return AuthorizationUser()


@pytest.fixture()
def update_real_user():
    return UpdateUserData()


@pytest.fixture()
def order():
    return CreateOrder()


@pytest.fixture()
def get_user_orders():
    return GetOrdersSpecificUser()


@pytest.fixture()
def delete_user():
    def delete(email, password, token):
        payload = {"email": email, "password": password}
        requests.delete(f"{Url.BASE_URL}{Url.DELETE_USER}", headers={'Authorization': token}, data=payload)

    return delete
