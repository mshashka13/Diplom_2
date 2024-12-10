import allure
from data import ErrorMessage


@allure.feature('Тесты на создание пользователя')
class TestCreateUser:
    @allure.title('Успешное создание пользователя')
    def test_successful_create_user(self, created_user, delete_user):
        response, email, password, _, token = created_user.create_user()
        delete_user(email, password, token)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Ошибка при создании уже зарегистрированного пользователя')
    def test_error_create_user_again(self, created_user, delete_user):
        response, email, password, token = created_user.create_user_again()
        delete_user(email, password, token)
        assert response.status_code == 403 and response.json()["success"] == False and ErrorMessage.USER_ALREADY_EXISTS in response.text

    @allure.title('Ошибка при создании пользователя без email')
    def test_error_create_user_without_email(self, created_user):
        response = created_user.create_user_without_email()
        assert response.status_code == 403 and response.json()["success"] == False and ErrorMessage.MISSING_FIELDS in response.text

    @allure.title('Ошибка при создании пользователя без пароля')
    def test_error_create_user_without_password(self, created_user):
        response = created_user.create_user_without_password()
        assert response.status_code == 403 and response.json()["success"] == False and ErrorMessage.MISSING_FIELDS in response.text

    @allure.title('Ошибка при создании пользователя без имени')
    def test_error_create_user_without_username(self, created_user):
        response = created_user.create_user_without_username()
        assert response.status_code == 403 and response.json()["success"] == False and ErrorMessage.MISSING_FIELDS in response.text
