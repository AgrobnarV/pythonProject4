import pytest

from OpenUserApi2.lib.assertions import Assertions
from OpenUserApi2.lib.basecase import BaseCase
from OpenUserApi2.lib.logger import Logger
from OpenUserApi2.lib.my_requests import MyRequests


class TestUserAuth(BaseCase):
    exclude_params = [
        "no_cookie",
        "no_token"
    ]

    def setup(self):
        data = {"email": "vinkotov@example.com", "password": "1234"}
        response = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response, "auth_sid")
        self.token = self.get_headers(response, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response, "user_id")

    # позитивный авторизационный тест
    def test_auth_user(self):

        response2 = MyRequests.get("/user/auth", headers={"x-csrf-token": self.token},
                                   cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(response2, "user_id", self.user_id_from_auth_method,
                                             "Значения user_id не совпадают в запросах")

    # негативные авторизационные тесты. Проверяют авторизацию, не отправляя куки или токен в запрос ручки /auth
    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, condition):

        if condition == "no_cookie":
            response = MyRequests.get("/user/auth", headers={"x-csrf-token": self.token})
        else:
            response = MyRequests.get("/user/auth", cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(response, "user_id", 0, f"Юзер не авторизовался с условием {condition}")
