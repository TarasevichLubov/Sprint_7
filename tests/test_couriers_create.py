import pytest
from clients.api_client import ApiClient
from data import TestData, EndPointData
import allure


class TestCouriers:

    path = EndPointData.PATH_CREATE_COURIERS
    # курьера можно создать

    @allure.title("Успешная регистрация нового курьера с валидными данными.")
    @allure.description("Курьер создан.")
    def test_couriers_create(self, register_new_courier_and_return_login_password):
        assert len(register_new_courier_and_return_login_password) > 0

    # нельзя создать двух одинаковых курьеров;
    @allure.title("Регистрация нового курьера с ранее созданными параметрами невозможна.")
    @allure.description("Нельзя создать двух курьеров.")
    def test_double_couriers_create(self, register_new_courier_and_return_login_password):
        api = ApiClient()
        payload_data = {"login": register_new_courier_and_return_login_password[0],
                        "password": register_new_courier_and_return_login_password[1],
                        "firstName": register_new_courier_and_return_login_password[2]}
        response = api.post(self.path, payload_data)
        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title("Регистрация нового курьера с одинаковым логином выдаст ошибку.")
    @allure.description("Нельзя создать курьеров с одинаковым логином.")
    def test_couriers_create_double_login(self, register_new_courier_and_return_login_password):
        api = ApiClient()
        payload_data = {"login": register_new_courier_and_return_login_password[0], "password": '123456', "firstName": ''}
        response = api.post(self.path, payload_data)
        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    # чтобы создать курьера, нужно передать в ручку все обязательные поля;
    # если одного из полей нет, запрос возвращает ошибку;
    @allure.title("Регистрация нового курьера с пустыми данными выдаст ошибку.")
    @allure.description("Нельзя создать курьеров без заполненных данных")
    @pytest.mark.parametrize('payload', TestData.payload_data)
    def test_required_field(self, payload):
        api = ApiClient()
        response = api.post(self.path, payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    # запрос возвращает правильный код ответа;
    # успешный запрос возвращает {"ok":true};
    @allure.title("Успешная регистрация нового курьера с валидными данными возвращает правильный код ответа.")
    @allure.description("В ответ возвращается верный ответ")
    def test_success_register(self):
        api = ApiClient()
        response = api.post(self.path, TestData.payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}
