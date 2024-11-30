import allure


@allure.title('Тесты на изменение данных пользователя')
class TestUpdateUser:
    @allure.title('Успешное изменение email пользователя')
    def test_update_user_data_change_email(self, update_real_user, delete_user):
        status_code, json, email, password, token = update_real_user.update_user_data_change_email()
        delete_user(email, password, token)
        assert status_code == 200 and json["success"] == True

    @allure.title('Успешное изменение пароля пользователя')
    def test_update_user_data_change_password(self, update_real_user, delete_user):
        status_code, json, email, password, token = update_real_user.update_user_data_change_password()
        delete_user(email, password, token)
        assert status_code == 200 and json["success"] == True

    @allure.title('Успешное изменение имени пользователя')
    def test_update_user_data_change_username(self, update_real_user, delete_user):
        status_code, json, email, password, token = update_real_user.update_user_data_change_username()
        delete_user(email, password, token)
        assert status_code == 200 and json["success"] == True

    @allure.title('Ошибка при изменении данных без авторизации')
    def test_error_update_user_data_without_authorization(self, update_real_user, delete_user):
        status_code, json, text, email, password, token = update_real_user.update_user_data_without_authorization()
        message = "You should be authorised"
        delete_user(email, password, token)
        assert status_code == 401 and json["success"] == False and message in text

    @allure.title('Ошибка при изменении email на существующий в базе email')
    def test_update_user_data_change_email_already_existing(self, update_real_user, delete_user):
        status_code, json, text, email, password, token = update_real_user.update_user_data_change_email_already_existing()
        message = "User with such email already exists"
        delete_user(email, password, token)
        assert status_code == 403 and json["success"] == False and message in text
