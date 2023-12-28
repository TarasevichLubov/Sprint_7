import random


class ConstantData:
    BASE_URL = "http://qa-scooter.praktikum-services.ru/"
    DEFAULT_HEADERS = {"accept": "application/json", "Content-Type": "application/json"}
    BASE_USER = {"login": 'TestingUser', "password": '123456', "firstName": 'Sam'}
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
