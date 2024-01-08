import pytest
from clients.api_client import ApiClient
from data import TestData, EndPointData
import allure


class TestOrders:
    path = EndPointData.PATH_ORDER

    # можно указать один из цветов — BLACK или GREY;
    # можно указать оба цвета;
    # можно совсем не указывать цвет;
    # тело ответа содержит track
    @allure.title("Успешное создание заказа с валидными данными.")
    @allure.description("Страница заказа")
    @pytest.mark.parametrize('payload', TestData.orders_data)
    def test_required_field(self, payload):
        api = ApiClient()
        response = api.post(self.path, payload)
        assert response.status_code == 201
        assert 'track' in response.text
