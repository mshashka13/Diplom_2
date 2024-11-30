# URL StellarBurgers, ручки API
class Url:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api/"
    GET_DATA_INGREDIENTS = "ingredients"
    CREATE_ORDER = "orders"
    RECOVERY_AND_RESET_PASSWORD = "password-reset"
    CREATE_USER = "auth/register"
    AUTHORIZATION = "auth/login"
    REGISTRATION = "auth/register"
    LOGOUT = "auth/logout"
    REFRESH_TOKEN = "auth/token"
    GET_DATA_USER = "auth/user"
    UPDATE_DATA_USER = "auth/user"
    DELETE_USER = "auth/user"
    GET_ALL_ORDERS = "orders/all"
    GET_ORDERS_SPECIFIC_USER = "orders"


# Данные для создания заказов
class Orders:
    ORDER_1 = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa75"]}
    ORDER_2 = {"ingredients": ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa79", "61c0c5a71d1f82001bdaaa76"]}
    ORDER_3 = {"ingredients": ["61c0c5a"]}
