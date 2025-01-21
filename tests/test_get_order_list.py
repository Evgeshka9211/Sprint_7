import allure
import requests
import urls

class TestOrderList:
    @allure.title("Получение списка заказов")
    def test_return_list_order(self):
        process_success = False
        try:
            order_list = requests.get(urls.BASE_URL + urls.ORDER_LIST, timeout=20)
            process_success = order_list.status_code == 200 and order_list.json()["orders"] != []
        except requests.exceptions.Timeout:
            print("Timed out")
        assert process_success == True