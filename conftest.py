import allure
import pytest
import helper
import scooter_api
import urls
import requests

@allure.step("Создание шаблонного курьера")
@pytest.fixture(scope='function')
def default_courier():g
    body = helper.create_courier()
    courier_response = scooter_api.create_courier(body)
    login_body = body.copy()
    login_body.pop("firstName", None)
    id_courier = requests.post(urls.BASE_URL + urls.COURIER_LOGIN, json=login_body).json().get("id")
    yield courier_response
    requests.delete(urls.BASE_URL + urls.COURIER_DELETE + str(id_courier))