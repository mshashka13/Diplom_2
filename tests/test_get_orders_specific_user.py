import allure


@allure.title('Тесты на получение заказов конкретного пользователя')
class TestGetOrdersSpecificUser:
    @allure.title('Успешное получение заказов конкретного пользователя с авторизацией')
    def test_get_orders_specific_user_with_authorizartion(self, get_user_orders, delete_user):
        status_code, json, email, password, token = get_user_orders.get_orders_specific_user_with_authorizartion()
        delete_user(email, password, token)
        assert status_code == 200 and json["success"] == True

    @allure.title('Ошибка при получении заказов конкретного пользователя без авторизации')
    def test_error_get_orders_specific_user_without_authorizartion(self, get_user_orders):
        status_code, json, text = get_user_orders.get_orders_specific_user_without_authorizartion()
        message = "You should be authorised"
        assert status_code == 401 and json["success"] == False and message in text
