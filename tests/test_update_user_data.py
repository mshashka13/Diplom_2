import allure
from data import ErrorMessage


@allure.feature('Тесты на изменение данных пользователя')
class TestUpdateUser:
    @allure.title('Успешное изменение email пользователя')
    def test_update_user_data_change_email(self, update_authorized_user, delete_user, created_user, authorized_user):
        _, email, password, _, token = created_user.create_user()
        authorized_user.authorize_user(email, password)
        response = update_authorized_user.update_user_data_change_email(token)
        delete_user(email, password, token)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Успешное изменение пароля пользователя')
    def test_update_user_data_change_password(self, update_authorized_user, delete_user, created_user, authorized_user):
        _, email, password, _, token = created_user.create_user()
        authorized_user.authorize_user(email, password)
        response = update_authorized_user.update_user_data_change_password(token)
        delete_user(email, password, token)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Успешное изменение имени пользователя')
    def test_update_user_data_change_username(self, update_authorized_user, delete_user, created_user, authorized_user):
        _, email, password, _, token = created_user.create_user()
        authorized_user.authorize_user(email, password)
        response = update_authorized_user.update_user_data_change_username(token)
        delete_user(email, password, token)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Ошибка при изменении данных без авторизации')
    def test_error_update_user_data_without_authorization(self, update_authorized_user, delete_user, created_user):
        _, email, password, _, token = created_user.create_user()
        response = update_authorized_user.update_user_data_without_authorization(email, password)
        delete_user(email, password, token)
        assert response.status_code == 401 and response.json()["success"] == False and ErrorMessage.AUTHORIZATION_REQUIRED in response.text

    @allure.title('Ошибка при изменении email на существующий в базе email')
    def test_update_user_data_change_email_already_existing(self, update_authorized_user, delete_user, created_user, authorized_user):
        _, email, password, _, token = created_user.create_user()
        authorized_user.authorize_user(email, password)
        _, new_email, _, _, _ = created_user.create_user()
        response = update_authorized_user.update_user_data_change_email_already_existing(new_email, token)
        delete_user(email, password, token)
        assert response.status_code == 403 and response.json()["success"] == False and ErrorMessage.EMAIL_ALREADY_EXISTS in response.text
