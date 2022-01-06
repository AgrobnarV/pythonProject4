import json.decoder

from requests import Response


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Не найдены куки с именем {cookie_name} в ответе"
        return response.cookies[cookie_name]

    def get_headers(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Не найден хэдер с именем {headers_name} в ответе"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        # убеждаемся что ответ пришел в формате JSON
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Текст ответа не в формате JSON. Фактический текст '{response.text}'"

        assert name in response_as_dict, f"В ответе нет ключа '{name}'"

        return response_as_dict[name]
