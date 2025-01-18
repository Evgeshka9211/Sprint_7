import allure
import pytest
import requests
import scooter_api
import urls

class TestCreateOrder:
    @allure.title("Создание заказа, разные самокаты. Успешно.")
    @pytest.mark.parametrize("color", [
        pytest.param(["BLACK"]),
        pytest.param(["GREY"]),
        pytest.param(["BLACK","GREY"]),
        pytest.param([]),
    ])
    def test_choice_color_in_success_order(self, color):
        color_body = {"color": color}
        create_color_order = scooter_api.create_order(color_body)
        assert create_color_order.status_code == 201 and create_color_order.json()["track"] != None


class TestOrderList:
    @allure.title("Получение списка заказов")
    def test_return_list_order(self):
        order_list = requests.get(urls.BASE_URL + urls.ORDER_LIST)
        assert order_list.status_code == 200 and order_list.json()["orders"] != []
