import allure
from clients.api_client import ApiClient
from base_models import Orders


class TestOrder:
    path_track = "api/v1/orders/track"
    path_order = "api/v1/orders"

    @allure.description("Тестирование ответа из перечня заказов")
    def test_required_field(self):
        api = ApiClient()
        response_get = api.get(self.path_order)
        assert Orders.model_validate(response_get.json()["orders"][1])
