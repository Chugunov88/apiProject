"""Методы для проверки ответов наших запросов"""
import json
from requests import Response

class Checking():

    """Метод для проверки """
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Успешно!!! статус код = " + str(response.status_code))
        else:
            print("Провал!!! статус код = " + str(response.status_code))


    """Метод для проверки наличиния полей в ответе запроса"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")


    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен!!!")

        """Метод для проверки значений обязательных полей в ответе запросапо заданному слову"""

    @staticmethod
    def check_json_search_world_in_value(response: Response, field_name, search_world):
        check = response.json()
        check_info = check.get(field_name)
        if search_world in check_info:
            print("Слово " + search_world + " присутствует !!!")
        else:
            print("Слово " + search_world + "отсутствует !!!")