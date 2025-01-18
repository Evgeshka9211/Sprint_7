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
    ERROR_NAME_USED_ALREADY = "Учетная запись с таким именем уже существует"
    ERROR_EXISTS_REQUIRED_REGISTER_DATA = "Отсутствуют обязательные поля для регистрации"
    ERROR_DATA_NOT_FOUND = "Учетная запись не найдена"
    ERROR_EXISTS_REQUIRED_LOGIN_DATA = "Отсутствуют обязательные поля для авторизации"