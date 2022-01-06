import requests


class TestHomeworkHeaders:
    def test_homework_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        assert response.status_code == 200, f"Неверный статус код"
        print(dict(response.headers))

        expected_header = "x-secret-homework-header"
        expected_header_value = "Some secret value"
        actual_header_value = response.headers.get("x-secret-homework-header")

        assert expected_header in response.headers, f"В ответе не возвращается хидэр {expected_header}"
        assert expected_header_value in response.headers.values(), f"В ответе возвращается неверное значение хидэра {expected_header}"
        assert actual_header_value == expected_header_value, "В ответе отсутствует или возвращается неверный хидэр"
