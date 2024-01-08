import random


class ConstantData:
    DEFAULT_HEADERS = {"accept": "application/json", "Content-Type": "application/json"}
    BASE_USER = {"login": 'TestingUser', "password": '123456', "firstName": 'Sam'}


class TestData:
    base_incorrect_data = [
        {"login": 'TestingUser', "password": '', "firstName": 'Sam'},
        {"login": '', "password": '123456', "firstName": 'Sam'}
    ]
    wrong_data = [
        {"login": 'TestingUser_wrong', "password": '123456', "firstName": 'Sam'},
        {"login": 'TestingUser', "password": '1234566', "firstName": 'Sam'}
    ]

    test_data = 'TEST' + str(random.randint(100, 999))
    payload_data = [
        {"login": test_data, "password": '', "firstName": 'Sam'},
        {"login": '', "password": test_data, "firstName": 'Sam'}
    ]

    payload = {"login": test_data, "password": test_data, "firstName": 'Sam'}

    orders_data = [
        {"firstName": "Sam", "lastName": "Bas", "address": "Moscow, 142 apt.", "metroStation": 4,
         "phone": "+7 800 355 35 35", "rentTime": 5, "deliveryDate": "2020-06-06",
         "comment": "come soon", "color": ["BLACK"]},
        {"firstName": "Sam", "lastName": "Bas", "address": "Moscow, 142 apt.", "metroStation": 4,
         "phone": "+7 800 355 35 35", "rentTime": 5, "deliveryDate": "2020-06-06",
         "comment": "come soon", "color": ["BLACK", "GREY"]},
        {"firstName": "Sam", "lastName": "Bas", "address": "Moscow, 142 apt.", "metroStation": 4,
         "phone": "+7 800 355 35 35", "rentTime": 5, "deliveryDate": "2020-06-06",
         "comment": "come soon", "color": []}
    ]


class EndPointData:
    BASE_URL = "http://qa-scooter.praktikum-services.ru/"
    PATH_CREATE_COURIERS = "api/v1/courier"
    PATH_COURIERS_LOGIN = "api/v1/courier/login"
    PATH_TRACK = "api/v1/orders/track"
    PATH_ORDER = "api/v1/orders"
