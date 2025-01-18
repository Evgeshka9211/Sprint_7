import allure
import requests
import data
import helper
import urls
import json


class TestLoginCourier:
    @allure.title("Авторизация курьера. Успешно.")
    def test_success_login(self, default_courier):
        courier_body_dict = json.loads(default_courier.request.body.decode('utf-8'))
        courier_login = requests.post(urls.BASE_URL + urls.COURIER_LOGIN, json=courier_body_dict)
        assert courier_login.status_code == 200 and courier_login.json()["id"] is not None


    @allure.title("Авторизация курьера. Ошибка. Неверный login.")
    def test_fail_with_wrong_login(self, default_courier):
        default_courier_body = default_courier.request.body
        default_courier_body_dict = json.loads(default_courier_body)
        requests.post(urls.BASE_URL + urls.COURIER_CREATE, default_courier_body)
        body_login = default_courier_body_dict.copy()
        body_login["login"] = "Courier"
        courier_login = requests.post(urls.BASE_URL + urls.COURIER_LOGIN, json=body_login)
        assert courier_login.status_code == 404 and courier_login.json()["message"] == data.ErrorMessages.ERROR_DATA_NOT_FOUND


    @allure.title("Авторизация курьера. Ошибка. Неверный password.")
    def test_fail_with_wrong_password(self, default_courier):
        default_courier_body = default_courier.request.body
        courier_body_dict = json.loads(default_courier_body)
        requests.post(urls.BASE_URL + urls.COURIER_CREATE, default_courier_body)
        courier_body_dict["password"] = "54321"
        courier_password = requests.post(urls.BASE_URL + urls.COURIER_LOGIN, json=courier_body_dict)
        assert courier_password.status_code == 404 and courier_password.json()["message"] == data.ErrorMessages.ERROR_DATA_NOT_FOUND


    @allure.title("Авторизация курьера. Ошибка. Пустой login.")
    def test_fail_with_empty_login(self, default_courier):
        default_courier_body = default_courier.request.body
        courier_body_dict = json.loads(default_courier_body)
        requests.post(urls.BASE_URL + urls.COURIER_CREATE, default_courier_body)
        courier_body_dict["login"] = ""
        courier_login = requests.post(urls.BASE_URL + urls.COURIER_LOGIN, json=courier_body_dict)
        assert courier_login.status_code == 400 and courier_login.json()["message"] == data.ErrorMessages.ERROR_EXISTS_REQUIRED_LOGIN_DATA


    @allure.title("Авторизация курьера. Ошибка. Пустой password.")
    def test_fail_with_empty_password(self, default_courier):
        courier_response = default_courier
        courier_body_dict = json.loads(courier_response.request.body)
        courier_body_dict["password"] = ""
        courier_password = requests.post(urls.BASE_URL + urls.COURIER_LOGIN, json=courier_body_dict)
        assert courier_password.status_code == 400 and courier_password.json()["message"] == data.ErrorMessages.ERROR_EXISTS_REQUIRED_LOGIN_DATA


    @allure.title("Авторизация курьера. Ошибка. Курьер не найден.")
    def test_fail_nonexistent_courier_login(self):
        body = helper.create_courier()
        courier_login = requests.post(urls.BASE_URL + urls.COURIER_LOGIN, json=body)
        assert courier_login.status_code == 404 and courier_login.json()["message"] == data.ErrorMessages.ERROR_DATA_NOT_FOUND