import requests
from data import Url, Orders
from methods.authorization_user import AuthorizationUser


# Создание заказа
class CreateOrder:
    # Получить ингредиенты
    def get_ingredients(self):
        response = requests.get(f"{Url.BASE_URL}{Url.GET_DATA_INGREDIENTS}")
        return response.json()

    # Создать заказ с авторизацией
    def create_order_authorization_user(self, params):
        user = AuthorizationUser()
        user.authorization_user()
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_ORDER}", data=params)
        return response.status_code, response.json()

    # Создать заказ без авторизации
    def create_order_without_authorization(self, params):
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_ORDER}", data=params)
        return response.status_code, response.json()

    # Создать заказ без иннгредиентов
    def create_order_without_ingredients(self):
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_ORDER}", data={})
        return response.status_code, response.json(), response.text

    # Создать заказ с некорретным хешем ингредиентов
    def create_order_with_incorrect_hash_ingredient(self):
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_ORDER}", data=Orders.ORDER_3)
        return response.status_code
