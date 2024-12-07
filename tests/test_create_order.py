import allure
import pytest
from data import Orders


@allure.title('Тесты на создание заказа')
class TestCreateOrder:
    @pytest.mark.parametrize('order_data', [Orders.ORDER_1, Orders.ORDER_2])
    @allure.title('Успешное создание заказа с авторизацией')
    def test_create_order_authorization_user(self, order_data, order):
        status_code, json = order.create_order_authorization_user(order_data)
        assert status_code == 200 and json["success"] == True

    @pytest.mark.parametrize('order_data', [Orders.ORDER_1, Orders.ORDER_2])
    @allure.title('Успешное создание заказа без авторизации')
    def test_create_order_without_authorization(self, order_data, order):
        status_code, json = order.create_order_without_authorization(order_data)
        assert status_code == 200 and json["success"] == True

    @allure.title('Ошибка при создании заказа без ингредиентов')
    def test_error_create_order_without_ingredients(self, order):
        status_code, json, text = order.create_order_without_ingredients()
        message = "Ingredient ids must be provided"
        assert status_code == 400 and json["success"] == False and message in text

    @allure.title('Ошибка при создании заказа с неверным хешем ингредиентов')
    def test_error_create_order_with_incorrect_hash_ingredient(self, order):
        status_code = order.create_order_with_incorrect_hash_ingredient()
        assert status_code == 500
