import allure
from data import ErrorMessage


@allure.feature('Тесты на авторизацию пользователя')
class TestAuthorizationUser:
    @allure.title('Успешная авторизация пользователя')
    def test_successful_authorization_user(self, created_user, authorized_user, delete_user):
        _, email, password, _, token = created_user.create_user()
        response = authorized_user.authorize_user(email, password)
        delete_user(email, password, token)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Ошибка при авторизации пользователя с некорретным email')
    def test_authorization_with_invalid_email(self, created_user, authorized_user):
        _, email, password, _, _ = created_user.create_user()
        invalid_email = "email"
        response = authorized_user.authorize_user(invalid_email, password)
        assert response.status_code == 401 and response.json()['success'] == False and ErrorMessage.INCORRECT_USER_DATA in response.text

    def test_authorization_with_invalid_password(self, created_user, authorized_user):
        _, email, password, _, _ = created_user.create_user()
        invalid_password = "000"
        response = authorized_user.authorize_user(email, invalid_password)
        assert response.status_code == 401 and response.json()['success'] == False and ErrorMessage.INCORRECT_USER_DATA in response.text
