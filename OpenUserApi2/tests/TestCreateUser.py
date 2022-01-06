from datetime import datetime

import requests
from OpenUserApi2.lib.BaseCase import BaseCase
from OpenUserApi2.lib.Assertions import Assertions


class TestUserRegister(BaseCase):
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    # проверить что пользователь успешно создался
    def test_create_user_success(self):
        data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_json_has_key(response, "id")
        Assertions.assert_code_status(response, 200)

    # проверить что нельзя создать пользователя с уже созданным email
    def test_check_create_user_with_email(self):
        email = "vinkotov@example.com"
        data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Неподдерживаемый контент {response.content}"
