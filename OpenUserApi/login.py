import pytest
import requests


class TestUserAuth:
    # позитивный авторизационный тест
    def test_auth_user(self):
        data = {"email": "vinkotov@example.com", "password": "1234"}
        response = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response.cookies, "Нет кук авторизации в ответе"
        assert "x-csrf-token" in response.headers, "CSRF токен не найден в заголовках ответа"
        assert "user_id" in response.json(), "Не найден юзер айди в теле ответа ручки login"

        auth_sid = response.cookies.get("auth_sid")
        token = response.headers.get("x-csrf-token")
        user_id_from_auth_method = response.json()["user_id"]

        response2 = requests.get("https://playground.learnqa.ru/api/user/auth", headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})

        assert "user_id" in response.json(), "Не найден юзер айди в теле ответа ручки auth"
        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_auth_method == user_id_from_check_method, "Значения user_id не совпадают в запросах"

    exclude_params = [
        "no_cookie",
        "no_token"
    ]

    @pytest.mark.parametrize("condition", exclude_params)
    # негативные авторизационные тесты. Проверяют авторизацию, не отправляя куки или токен в запрос ручки /auth
    def test_negative_auth_check(self, condition):
        data = {"email": "vinkotov@example.com", "password": "1234"}
        response = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response.cookies, "Нет кук авторизации в ответе"
        assert "x-csrf-token" in response.headers, "CSRF токен не найден в заголовках ответа"
        assert "user_id" in response.json(), "Не найден юзер айди в теле ответа ручки login"

        auth_sid = response.cookies.get("auth_sid")
        token = response.headers.get("x-csrf-token")

        if condition == "no_cookie":
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth", headers={"x-csrf-token": token})
        else:
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth", cookies={"auth_sid": auth_sid})

        assert "user_id" in response.json(), "Не найден юзер айди в теле ответа ручки login"
        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_check_method == 0, f"Юзер не авторизовался с условием {condition}"
