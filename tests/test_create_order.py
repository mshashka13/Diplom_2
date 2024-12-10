import allure
import pytest
from data import Orders, ErrorMessage


@allure.feature('Тесты на создание заказа')
class TestCreateOrder:
    @pytest.mark.parametrize('order_data', [Orders.ORDER_1, Orders.ORDER_2])
    @allure.title('Успешное создание заказа с авторизацией')
    def test_create_order_authorization_user(self, order_data, order, created_user, authorized_user):
        _, email, password, _, _ = created_user.create_user()
        authorized_user.authorize_user(email, password)
        response = order.create_order_authorization_user(order_data)
        assert response.status_code == 200 and response.json()["success"] == True

    @pytest.mark.parametrize('order_data', [Orders.ORDER_1, Orders.ORDER_2])
    @allure.title('Успешное создание заказа без авторизации')
    def test_create_order_without_authorization(self, order_data, order):
        response = order.create_order_without_authorization(order_data)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Ошибка при создании заказа без ингредиентов')
    def test_error_create_order_without_ingredients(self, order):
        response = order.create_order_without_ingredients()
        assert response.status_code == 400 and response.json()["success"] == False and ErrorMessage.MISSING_INGREDIENT_IDS in response.text

    @allure.title('Ошибка при создании заказа с неверным хешем ингредиентов')
    def test_error_create_order_with_invalid_hash_ingredient(self, order):
        response = order.create_order_with_invalid_hash_ingredient()
        assert response.status_code == 500
