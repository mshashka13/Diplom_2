import allure
import requests
from data import Url, Orders


# Создание заказа
class CreateOrder:
    @allure.step('Получить ингредиенты')
    def get_ingredients(self):
        response = requests.get(f"{Url.BASE_URL}{Url.GET_DATA_INGREDIENTS}")
        return response.json()

    @allure.step('оздать заказ с авторизацией')
    def create_order_authorization_user(self, params):
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_ORDER}", data=params)
        return response

    @allure.step('Создать заказ без авторизации')
    def create_order_without_authorization(self, params):
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_ORDER}", data=params)
        return response

    @allure.step('Создать заказ без иннгредиентов')
    def create_order_without_ingredients(self):
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_ORDER}", data={})
        return response

    @allure.step('Создать заказ с некорретным хешем ингредиентов')
    def create_order_with_invalid_hash_ingredient(self):
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_ORDER}", data=Orders.ORDER_3)
        return response
