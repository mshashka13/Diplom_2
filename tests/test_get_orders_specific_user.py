import allure
from data import ErrorMessage


@allure.feature('Тесты на получение заказов конкретного пользователя')
class TestGetOrdersSpecificUser:
    @allure.title('Успешное получение заказов конкретного пользователя с авторизацией')
    def test_get_orders_specific_user_with_authorization(self, created_user, get_user_orders, delete_user):
        _, email, password, _, token = created_user.create_user()
        response = get_user_orders.get_orders_specific_user_with_authorization(token)
        delete_user(email, password, token)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Ошибка при получении заказов конкретного пользователя без авторизации')
    def test_error_get_orders_specific_user_without_authorization(self, get_user_orders):
        response = get_user_orders.get_orders_specific_user_without_authorization()
        assert response.status_code == 401 and response.json()["success"] == False and ErrorMessage.AUTHORIZATION_REQUIRED in response.text
