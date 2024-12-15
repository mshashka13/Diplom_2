import allure
import requests
from data import Url


# Получение заказов конкретного пользователя
class GetOrdersSpecificUser:
    @allure.step('Получить заказы конкретного пользователя с авторизацией')
    def get_orders_specific_user_with_authorization(self, token):
        response = requests.get(f"{Url.BASE_URL}{Url.CREATE_ORDER}", headers={'Authorization': token})
        return response

    @allure.step('Получить заказы конкретного пользователя без авторизации')
    def get_orders_specific_user_without_authorization(self):
        response = requests.get(f"{Url.BASE_URL}{Url.CREATE_ORDER}")
        return response
