from OpenUserApi2.lib.assertions import Assertions
from OpenUserApi2.lib.basecase import BaseCase
from OpenUserApi2.lib.my_requests import MyRequests
import allure


@allure.epic("Тесты на изменение залогированного пользователя")
class TestUserEdit(BaseCase):
    @allure.description(
        "Тест регенит пользователя, авторизуется под ним, редактирует имя пользователя и проверяет пользовательское новое имя")
    def test_edit_just_created_user(self):
        # Register
        register_data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response, "id")

        # Login
        login_data = {
            "email": email,
            "firstName": first_name,
            "password": password,
            "user_id": user_id
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_headers(response2, "x-csrf-token")

        # Edit
        new_name = "Changed Name"
        response3 = MyRequests.put(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid},
                                   data={"firstName": new_name})

        Assertions.assert_code_status(response3, 200)

        # Get
        response4 = MyRequests.get(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_json_value_by_name(response4, "firstName", new_name,
                                             "Неверное имя пользователя после редактирования")
