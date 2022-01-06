import requests


class TestHomeworkCookie:
    def test_homework_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        assert response.status_code == 200, f"Неправильный статус код"
        print(dict(response.cookies))

        expected_cookie = "HomeWork"
        expected_cookie_value = "hw_value"
        actual_cookie_value = response.cookies.get("HomeWork")

        assert expected_cookie in response.cookies, f"В ответе пришел неподдерживаемый куки"
        assert expected_cookie_value in response.cookies.values(), f"В ответе пришло неверное значение куки Homework"
        assert actual_cookie_value == expected_cookie_value, "В ответе пришло неверное значение куки Homework"
