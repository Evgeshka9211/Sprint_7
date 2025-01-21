import allure
import requests
import data
import helper
import scooter_api
import urls

class TestCreateCourier:
    @allure.title("Добавление нового курьера. Успешно.")
    def test_success_create_courier(self, default_courier):
        create_courier_request = default_courier
        assert create_courier_request.status_code == 201 and create_courier_request.json()["ok"] == True


    @allure.title("Добавление нового курьера. Ошибка. Запись уже существует.")
    def test_create_duplicate_courier(self):
        body = helper.create_courier()
        requests.post(urls.BASE_URL + urls.COURIER_CREATE, body)
        duplicate_courier_request = scooter_api.create_courier(body)
        login_body = body.copy()
        login_body.pop("firstName", None)
        id_courier = requests.post(urls.BASE_URL + urls.COURIER_LOGIN, json=login_body).json().get("id")
        requests.delete(urls.BASE_URL + urls.COURIER_DELETE + str(id_courier))
        assert duplicate_courier_request.status_code == 409 and duplicate_courier_request.json()["message"] == data.ErrorMessages.ERROR_NAME_USED_ALREADY


    @allure.title("Добавление нового курьера. Ошибка. Не указан login.")
    def test_empty_login_create_courier(self):
        body_login = helper.ChangeTestDataHelper.modify_create_courier_body("login", "")
        empty_login_courier_request = scooter_api.create_courier(body_login)
        assert empty_login_courier_request.status_code == 400 and empty_login_courier_request.json()["message"] == data.ErrorMessages.ERROR_EXISTS_REQUIRED_REGISTER_DATA


    @allure.title("Добавление нового курьера. Ошибка. Не указан password.")
    def test_empty_password_create_courier(self):
        body_pass = helper.ChangeTestDataHelper.modify_create_courier_body("password", "")
        empty_password_courier_request = scooter_api.create_courier(body_pass)
        assert empty_password_courier_request.status_code == 400 and empty_password_courier_request.json()[
            "message"] == data.ErrorMessages.ERROR_EXISTS_REQUIRED_REGISTER_DATA


    @allure.title("Добавление нового курьера. Ошибка. Не указан firstname.")
    def test_empty_firstname_create_courier(self):
        body_firstname = helper.ChangeTestDataHelper.modify_create_courier_body("firstname", "")
        empty_firstname_courier_request = scooter_api.create_courier(body_firstname)
        assert empty_firstname_courier_request.status_code == 400 and empty_firstname_courier_request.json()[
            "message"] == data.ErrorMessages.ERROR_EXISTS_REQUIRED_REGISTER_DATA