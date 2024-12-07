import allure


@allure.title('Тесты на авторизацию пользователя')
class TestAuthorizationUser:
    @allure.title('Успешная авторизация пользователя')
    def test_successful_authorization_user(self, real_user, delete_user):
        status_code, json, email, password, token = real_user.authorization_user()
        delete_user(email, password, token)
        assert status_code == 200 and json['success'] == True

    @allure.title('Ошибка при авторизации пользователя с некорретным email')
    def test_error_authorization_user_with_incorrect_email(self, real_user, delete_user):
        status_code, json, text, email, password, token = real_user.authorization_user_with_incorrect_email()
        message = "email or password are incorrect"
        delete_user(email, password, token)
        assert status_code == 401 and json['success'] == False and message in text

    @allure.title('Ошибка при авторизации пользователя с некорретным паролем')
    def test_error_authorization_user_with_incorrect_password(self, real_user, delete_user):
        status_code, json, text, email, password, token = real_user.authorization_user_with_incorrect_password()
        message = "email or password are incorrect"
        delete_user(email, password, token)
        assert status_code == 401 and json['success'] == False and message in text
