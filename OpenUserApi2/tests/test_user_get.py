import allure

from OpenUserApi2.lib.assertions import Assertions
from OpenUserApi2.lib.basecase import BaseCase
from OpenUserApi2.lib.my_requests import MyRequests


@allure.epic("Тесты на детали инфы о пользователе")
class TestUserInfo(BaseCase):
    def setup(self):
        data = {"email": "vinkotov@example.com", "password": "1234"}
        response1 = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_headers(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    @allure.description("Тест проверяет, что в ответе ручки приходят нужные ключи")
    def test_check_user_details_not_auth(self):
        response2 = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response2, "username")
        Assertions.assert_json_has_not_key(response2, "email")
        Assertions.assert_json_has_not_key(response2, "firstName")
        Assertions.assert_json_has_not_key(response2, "lastName")

    @allure.description("Тест проверяет результат авторизации под единым email и паролем")
    def test_get_user_details_auth(self):
        response3 = MyRequests.get(f"/user/{self.user_id_from_auth_method}",
                                   headers={"x-csrf-token": self.token},
                                   cookies={"auth_sid": self.auth_sid})

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response3, expected_fields)
