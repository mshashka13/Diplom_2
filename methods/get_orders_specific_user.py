import requests
from methods.create_user import CreateUser
from data import Url


# Получение заказов конкретного пользователя
class GetOrdersSpecificUser:

    # Получить заказы конкретного пользователя с авторизацией
    def get_orders_specific_user_with_authorizartion(self):
        user = CreateUser()
        user.create_user()
        _, _, email, password, _, token = user.create_user()
        response = requests.get(f"{Url.BASE_URL}{Url.CREATE_ORDER}", headers={'Authorization': token})
        return response.status_code, response.json(), email, password, token

    # Получить заказы конкретного пользователя без авторизации
    def get_orders_specific_user_without_authorizartion(self):
        response = requests.get(f"{Url.BASE_URL}{Url.CREATE_ORDER}")
        return response.status_code, response.json(), response.text
