import allure
import requests
from data import Url


# Авторизация пользователя
class AuthorizationUser:
    @allure.step("Авторизация пользователя")
    def authorize_user(self, email, password):
        payload = {"email": email, "password": password}
        response = requests.post(f"{Url.BASE_URL}{Url.AUTHORIZATION}", data=payload)
        return response
