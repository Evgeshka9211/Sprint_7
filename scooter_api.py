import allure
import urls
import requests

@allure.step("Добавление курьера")
def create_courier(body):
    return requests.post(urls.BASE_URL+urls.COURIER_CREATE, json=body)

@allure.step("Создание нового заказа")
def create_order(order_body):
    return requests.post(urls.BASE_URL + urls.ORDER_CREATE, json=order_body)

@allure.step("Отмена заказа")
def cancel_order(order_cancel_body):
    url = urls.BASE_URL + urls.ORDER_CANCEL
    return requests.put(url, json=order_cancel_body)