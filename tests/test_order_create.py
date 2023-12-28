import pytest
from clients.api_client import ApiClient
from data import ConstantData
import allure


class TestOrders:
    path = "api/v1/orders"

    # можно указать один из цветов — BLACK или GREY;
    # можно указать оба цвета;
    # можно совсем не указывать цвет;
    # тело ответа содержит track
    @allure.description("Страница заказа")
    @pytest.mark.parametrize('payload', ConstantData.orders_data)
    def test_required_field(self, payload):
        api = ApiClient()
        response = api.post(self.path, payload)
        assert response.status_code == 201
        assert 'track' in response.text
