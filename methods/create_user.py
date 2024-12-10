import allure
import requests
import helpers
from data import Url


# Создание пользователя
class CreateUser:
    @allure.step('Создать пользователя')
    def create_user(self):
        email = f"{helpers.generate_random_string(7)}@yandex.ru"
        password = helpers.generate_random_integer()
        username = helpers.generate_random_string(10)
        payload = {"email": email, "password": password, "name": username}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_USER}", data=payload)
        token = response.json()["accessToken"]
        return response, email, password, username, token

    @allure.step('Создать уже зарегистрированного пользователя')
    def create_user_again(self):
        email = f"{self.create_user()[1]}"
        password = f"{self.create_user()[2]}"
        username = f"{self.create_user()[3]}"
        token = f"{self.create_user()[4]}"
        payload = {"email": email, "password": password, "name": username}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_USER}", data=payload)
        return response, email, password, token

    @allure.step('Создать пользователя без заполнения email')
    def create_user_without_email(self):
        password = helpers.generate_random_integer()
        username = helpers.generate_random_string(10)
        payload = {"email": '', "password": password, "name": username}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_USER}", data=payload)
        return response

    @allure.step('Создать пользователя без заполнения пароля')
    def create_user_without_password(self):
        email = f"{helpers.generate_random_string(7)}@yandex.ru"
        username = helpers.generate_random_string(10)
        payload = {"email": email, "password": '', "name": username}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_USER}", data=payload)
        return response

    @allure.step('Создать пользователя без заполнения имени')
    def create_user_without_username(self):
        email = f"{helpers.generate_random_string(7)}@yandex.ru"
        password = helpers.generate_random_integer()
        payload = {"email": email, "password": password, "name": ''}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_USER}", data=payload)
        return response
