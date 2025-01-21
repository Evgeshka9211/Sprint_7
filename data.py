class TestDataCreatingOrder:
    CREATE_ORDER_BODY = {
        "firstName": "Филипп",
        "lastName": "Преображенский",
        "address": "Пречистенка, 24",
        "metroStation": 1,
        "phone": "+78007555555",
        "rentTime": 10,
        "deliveryDate": "2020-06-06",
        "comment": "к 8:00",
        "color": ["BLACK"]
    }

class ErrorMessages:
    ERROR_NAME_USED_ALREADY = "Этот логин уже используется"
    ERROR_EXISTS_REQUIRED_REGISTER_DATA = "Недостаточно данных для создания учетной записи"
    ERROR_DATA_NOT_FOUND = "Учетная запись не найдена"
    ERROR_EXISTS_REQUIRED_LOGIN_DATA = "Недостаточно данных для входа"