import allure

from OpenUserApi2.lib.assertions import Assertions
from OpenUserApi2.lib.basecase import BaseCase
from OpenUserApi2.lib.my_requests import MyRequests


@allure.epic("Тесты на создание юзера")
class TestUserRegister(BaseCase):
    @allure.description("Тест проверяет успешное создание учетки")
    def test_create_user_success(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("Тест проверяет невозможность создать пользователя с уже созданным email")
    def test_check_create_user_with_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Неподдерживаемый контент {response.content}"
