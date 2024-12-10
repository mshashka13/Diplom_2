import allure
import requests
import helpers
from data import Url


# Изменение данных пользователя
class UpdateUserData:
    @allure.step('Изменить email пользователя')
    def update_user_data_change_email(self, token):
        new_email = helpers.generate_random_string(7)
        new_payload = {"email": new_email}
        response = requests.patch(f"{Url.BASE_URL}{Url.UPDATE_DATA_USER}", headers={'Authorization': token}, data=new_payload)
        return response

    @allure.step('Изменить пароль пользователя')
    def update_user_data_change_password(self, token):
        new_password = helpers.generate_random_string(7)
        new_payload = {"password": new_password}
        response = requests.patch(f"{Url.BASE_URL}{Url.UPDATE_DATA_USER}", headers={'Authorization': token}, data=new_payload)
        return response

    @allure.step('Изменить имя пользователя')
    def update_user_data_change_username(self, token):
        new_username = helpers.generate_random_string(7)
        new_payload = {"email": new_username}
        response = requests.patch(f"{Url.BASE_URL}{Url.UPDATE_DATA_USER}", headers={'Authorization': token}, data=new_payload)
        return response

    @allure.step('Изменить данные пользователя без авторизации')
    def update_user_data_without_authorization(self, email, password):
        payload = {"email": email, "password": password}
        response = requests.patch(f"{Url.BASE_URL}{Url.UPDATE_DATA_USER}", headers={'Authorization': ''}, data=payload)
        return response

    @allure.step('Изменить email пользователя на существующий в базе email')
    def update_user_data_change_email_already_existing(self, new_email, token):
        new_payload = {"email": new_email}
        response = requests.patch(f"{Url.BASE_URL}{Url.UPDATE_DATA_USER}", headers={'Authorization': token}, data=new_payload)
        return response
