import requests
import string
import random
from methods.create_user import CreateUser
from data import Url


# Изменение данных пользователя
class UpdateUserData:
    # Сгенерировать рандомную строку
    def generate_random_string(self, length):
        letters = string.ascii_letters
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # Изменить email пользователя
    def update_user_data_change_email(self):
        user = CreateUser()
        _, _, email, password, _, token = user.create_user()
        payload = {"email": email, "password": password}
        requests.post(f"{Url.BASE_URL}{Url.AUTHORIZATION}", data=payload)
        new_email = self.generate_random_string(7)
        new_payload = {"email": new_email}
        response = requests.patch(f"{Url.BASE_URL}{Url.UPDATE_DATA_USER}", headers={'Authorization': token},
                                  data=new_payload)
        return response.status_code, response.json(), email, password, token

    # Изменить пароль пользователя
    def update_user_data_change_password(self):
        user = CreateUser()
        _, _, email, password, _, token = user.create_user()
        payload = {"email": email, "password": password}
        requests.post(f"{Url.BASE_URL}{Url.AUTHORIZATION}", data=payload)
        new_password = self.generate_random_string(7)
        new_payload = {"password": new_password}
        response = requests.patch(f"{Url.BASE_URL}{Url.UPDATE_DATA_USER}", headers={'Authorization': token},
                                  data=new_payload)
        return response.status_code, response.json(), email, password, token

    # Изменить имя пользователя
    def update_user_data_change_username(self):
        user = CreateUser()
        _, _, email, password, _, token = user.create_user()
        payload = {"email": email, "password": password}
        requests.post(f"{Url.BASE_URL}{Url.AUTHORIZATION}", data=payload)
        new_username = self.generate_random_string(7)
        new_payload = {"email": new_username}
        response = requests.patch(f"{Url.BASE_URL}{Url.UPDATE_DATA_USER}", headers={'Authorization': token},
                                  data=new_payload)
        return response.status_code, response.json(), email, password, token

    # Изменить данные пользователя без авторизации
    def update_user_data_without_authorization(self):
        user = CreateUser()
        _, _, email, password, _, token = user.create_user()
        payload = {"email": email, "password": password}
        response = requests.patch(f"{Url.BASE_URL}{Url.UPDATE_DATA_USER}", headers={'Authorization': ''},
                                  data=payload)
        return response.status_code, response.json(), response.text, email, password, token

    # Изменить email пользователя на существующий в базе email
    def update_user_data_change_email_already_existing(self):
        user = CreateUser()
        _, _, email, password, _, token = user.create_user()
        payload = {"email": email, "password": password}
        requests.post(f"{Url.BASE_URL}{Url.AUTHORIZATION}", data=payload)
        _, _, new_email, new_password, _, _ = user.create_user()
        new_payload = {"email": new_email}
        response = requests.patch(f"{Url.BASE_URL}{Url.UPDATE_DATA_USER}", headers={'Authorization': token},
                                  data=new_payload)
        return response.status_code, response.json(), response.text, email, password, token
