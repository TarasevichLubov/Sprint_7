import pytest
from clients.api_client import ApiClient
from data import ConstantData
import allure


class TestUserLogin:
    path = "api/v1/courier/login"
    # курьер может авторизоваться;
    # успешный запрос возвращает id.

    @allure.description("Страница авторизации")
    def test_user_login(self):
        api = ApiClient()
        response = api.post(self.path, ConstantData.BASE_USER)
        assert response.status_code == 200
        assert response.json() == {'id': 245784}

    # если какого-то поля нет, запрос возвращает ошибку;
    # для авторизации нужно передать все обязательные поля;
    @allure.description("Логин с недостаточными данными")
    @pytest.mark.parametrize('payload', ConstantData.base_incorrect_data)
    def test_request_field(self, payload):
        api = ApiClient()
        response = api.post(self.path, payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    # система вернёт ошибку, если неправильно указать логин или пароль;
    # если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;
    @allure.description("Логин с неверными данными")
    @pytest.mark.parametrize('payload', ConstantData.wrong_data)
    def test_full_fields(self, payload):
        api = ApiClient()
        response = api.post(self.path, payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

