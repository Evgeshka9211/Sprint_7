import allure
import pytest
import scooter_api

class TestCreateOrder:
    @allure.title("Создание заказа, разные самокаты. Успешно.")
    @pytest.mark.parametrize("color",
    [
        pytest.param(["BLACK"]),
        pytest.param(["GREY"]),
        pytest.param(["BLACK","GREY"]),
        pytest.param([]),
    ])
    def test_choice_color_in_success_order(self, color):
        color_body = {"color": color}
        create_color_order = scooter_api.create_order(color_body)
        success_result = False
        if create_color_order.status_code == 201:
            track = create_color_order.json()["track"]
            if track > 0:
                success_result = True
                cancel_order_body = {"track": str(track)}
                scooter_api.cancel_order(cancel_order_body)
        assert success_result == True