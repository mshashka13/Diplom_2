import requests
import random
import string
from data import Url


# Создание пользователя
class CreateUser:
    # Сгенерировать рандомную строку
    def generate_random_string(self, length):
        letters = string.ascii_letters
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # Сгенерировать рандомное число
    def generate_random_integer(self):
        integer = f'{random.randint(100000, 999999)}'
        return integer

    # Создать пользователя
    def create_user(self):
        email = f"{self.generate_random_string(7)}@yandex.ru"
        password = self.generate_random_integer()
        username = self.generate_random_string(10)
        payload = {"email": email, "password": password, "name": username}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_USER}", data=payload)
        token = response.json()["accessToken"]
        return response.status_code, response.json(), email, password, username, token

    # Создать уже зарегистрированного пользователя
    def create_user_again(self):
        user = CreateUser()
        email = f"{user.create_user()[2]}"
        password = f"{user.create_user()[3]}"
        username = f"{user.create_user()[4]}"
        token = f"{user.create_user()[5]}"
        payload = {"email": email, "password": password, "name": username}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_USER}", data=payload)
        return response.status_code, response.json(), response.text, email, password, token

    # Создать пользователя без заполнения email
    def create_user_without_email(self):
        password = self.generate_random_integer()
        username = self.generate_random_string(10)
        payload = {"email": '', "password": password, "name": username}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_USER}", data=payload)
        return response.status_code, response.json(), response.text

    # Создать пользователя без заполнения пароля
    def create_user_without_password(self):
        email = f"{self.generate_random_string(7)}@yandex.ru"
        username = self.generate_random_string(10)
        payload = {"email": email, "password": '', "name": username}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_USER}", data=payload)
        return response.status_code, response.json(), response.text

    # Создать пользователя без заполнения имени
    def create_user_without_username(self):
        email = f"{self.generate_random_string(7)}@yandex.ru"
        password = self.generate_random_integer()
        payload = {"email": email, "password": password, "name": ''}
        response = requests.post(f"{Url.BASE_URL}{Url.CREATE_USER}", data=payload)
        return response.status_code, response.json(), response.text

