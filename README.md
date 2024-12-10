# Diplom_2
## __Тестирование API Stellar Burgers__ 
[API документация Stellar Burgers](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89 "Перейти")

___

### __Тесты (tests):__  
__*test_authorization_user - Тесты на авторизацию пользователя:*__
- test_successful_authorization_user - Успешная авторизация пользователя
- test_error_authorization_user_with_invalid_email - Ошибка при авторизации пользователя с некорретным email
- test_error_authorization_user_with_invalid_password - Ошибка при авторизации пользователя с некорретным паролем

__*test_ =create_order - Тесты на создание заказа:*__
- test_create_order_authorization_user - Успешное создание заказа с авторизацией
- test_create_order_without_authorization - Успешное создание заказа без авторизации
- test_error_create_order_without_ingredients - Ошибка при создании заказа без ингредиентов
- test_error_create_order_with_invalid_hash_ingredient - Ошибка при создании заказа с неверным хешем ингредиентов

__*test_create_user - Тесты на создание пользователя:*__
- test_successful_create_user - Успешное создание пользователя
- test_error_create_user_again - Ошибка при создании уже зарегистрированного пользователя
- test_error_create_user_without_email - Ошибка при создании пользователя без email
- test_error_create_user_without_password - Ошибка при создании пользователя без пароля
- test_error_create_user_without_username - Ошибка при создании пользователя без имени

__*test_get_orders_specific_user - Тесты на получение заказов конкретного пользователя:*__
- test_get_orders_specific_user_with_authorization - Успешное получение заказов конкретного пользователя с авторизацией
- test_error_get_orders_specific_user_without_authorization - Ошибка при получении заказов конкретного пользователя без авторизации

__*test_update_user_data - Тесты на изменение данных пользователя:*__
- test_update_user_data_change_email - Успешное изменение email пользователя
- test_update_user_data_change_password - Успешное изменение пароля пользователя
- test_update_user_data_change_username - Успешное изменение имени пользователя
- test_error_update_user_data_without_authorization - Ошибка при изменении данных без авторизации
- test_update_user_data_change_email_already_existing - Ошибка при изменении email на существующий в базе email



### __Методы (methods):__
__*authorization_user - Авторизация пользователя:*__
- authorize_user - Авторизация пользователя

__*create_order - Создание заказа:*__
- get_ingredients - Получить ингредиенты
- create_order_authorization_user - Создать заказ с авторизацией
- create_order_without_authorization - Создать заказ без авторизации
- create_order_without_ingredients - Создать заказ без иннгредиентов
- create_order_with_invalid_hash_ingredient - Создать заказ с некорретным хешем ингредиентов

__*create_user - Создание пользователя:*__
- create_user - Создать пользователя
- create_user_again - Создать уже зарегистрированного пользователя
- create_user_without_email - Создать пользователя без заполнения email
- create_user_without_password - Создать пользователя без заполнения пароля
- create_user_without_username - Создать пользователя без заполнения имени

__*get_orders_specific_user - Получение заказов конкретного пользователя:*__
- get_orders_specific_user_with_authorization - Получить заказы конкретного пользователя с авторизацией
- get_orders_specific_user_without_authorization - Получить заказы конкретного пользователя без авторизации

__*update_user_data - Изменение данных пользователя:*__
- update_user_data_change_email - Изменить email пользователя
- update_user_data_change_password - Изменить пароль пользователя
- update_user_data_change_username - Изменить имя пользователя
- update_user_data_without_authorization - Изменить данные пользователя без авторизации
- update_user_data_change_email_already_existing - Изменить email пользователя на существующий в базе email


### __Вспомогательные элементы:__
1. data - Константы: URL StellarBurgers - ручки API, Данные для создания заказов, Сообщения об ошибках
2. conftest - Фикстуры
3. helpers - Методы-помощники
3. README - описание тестируемого функционала
