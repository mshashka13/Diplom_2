import allure


@allure.title('Тесты на создание пользователя')
class TestCreateUser:
    @allure.title('Успешное создание пользователя')
    def test_successful_create_user(self, user, delete_user):
        status_code, json, email, password, _, token = user.create_user()
        delete_user(email, password, token)
        assert status_code == 200 and json["success"] == True

    @allure.title('Ошибка при создании уже зарегистрированного пользователя')
    def test_error_create_user_again(self, user, delete_user):
        status_code, json, text, email, password, token = user.create_user_again()
        message = "User already exists"
        delete_user(email, password, token)
        assert status_code == 403 and json["success"] == False and message in text

    @allure.title('Ошибка при создании пользователя без email')
    def test_error_create_user_without_email(self, user):
        status_code, json, text = user.create_user_without_email()
        message = "Email, password and name are required fields"
        assert status_code == 403 and json["success"] == False and message in text

    @allure.title('Ошибка при создании пользователя без пароля')
    def test_error_create_user_without_password(self, user):
        status_code, json, text = user.create_user_without_password()
        message = "Email, password and name are required fields"
        assert status_code == 403 and json["success"] == False and message in text

    @allure.title('Ошибка при создании пользователя без имени')
    def test_error_create_user_without_username(self, user):
        status_code, json, text = user.create_user_without_username()
        message = "Email, password and name are required fields"
        assert status_code == 403 and json["success"] == False and message in text
