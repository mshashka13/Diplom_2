import requests
from methods.create_user import CreateUser
from data import Url


# Авторизация пользователя
class AuthorizationUser:
    # Авторизация пользователя
    def authorization_user(self):
        user = CreateUser()
        _, _, email, password, _, token = user.create_user()
        payload = {"email": email, "password": password}
        response = requests.post(f"{Url.BASE_URL}{Url.AUTHORIZATION}", data=payload)
        return response.status_code, response.json(), email, password, token

    # Авторизация пользователя с некорректным email
    def authorization_user_with_incorrect_email(self):
        user = CreateUser()
        _, _, email, password, _, token = user.create_user()
        payload = {"email": password, "password": password}
        response = requests.post(f"{Url.BASE_URL}{Url.AUTHORIZATION}", data=payload)
        return response.status_code, response.json(), response.text, email, password, token

    # Авторизация пользователя с некорректным паролем
    def authorization_user_with_incorrect_password(self):
        user = CreateUser()
        _, _, email, password, _, token = user.create_user()
        payload = {"email": email, "password": email}
        response = requests.post(f"{Url.BASE_URL}{Url.AUTHORIZATION}", data=payload)
        return response.status_code, response.json(), response.text, email, password, token
