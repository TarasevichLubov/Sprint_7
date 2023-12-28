import pytest
from clients.api_client import ApiClient
from data import ConstantData
from conftest import register_new_courier_and_return_login_password
import allure


class TestCouriers:
    path = "api/v1/courier"
    # курьера можно создать

    @allure.description("Курьер создан")
    def test_couriers_create(self):
        new_courier = register_new_courier_and_return_login_password()
        assert len(new_courier) > 0

    # нельзя создать двух одинаковых курьеров;
    @allure.description("Нельзя создать двух курьеров")
    def test_double_couriers_create(self):
        new_courier = register_new_courier_and_return_login_password()
        api = ApiClient()
        payload_data = {"login": new_courier[0], "password": new_courier[1], "firstName": new_courier[2]}
        response = api.post(self.path, payload_data)
        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.description("Нельзя создать курьеров с одинаковым логином")
    def test_couriers_create_double_login(self):
        new_courier = register_new_courier_and_return_login_password()
        api = ApiClient()
        payload_data = {"login": new_courier[0], "password": '123456', "firstName": ''}
        response = api.post(self.path, payload_data)
        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    # чтобы создать курьера, нужно передать в ручку все обязательные поля;
    # если одного из полей нет, запрос возвращает ошибку;
    @allure.description("Нельзя создать курьеров без заполненных данных")
    @pytest.mark.parametrize('payload', ConstantData.payload_data)
    def test_required_field(self, payload):
        api = ApiClient()
        response = api.post(self.path, payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    # запрос возвращает правильный код ответа;
    # успешный запрос возвращает {"ok":true};
    @allure.description("В ответ возвращается верный ответ")
    def test_success_register(self):
        api = ApiClient()
        response = api.post(self.path, ConstantData.payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

