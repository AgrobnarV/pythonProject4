from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)  # печатаем текст ответа

# пробуем парсить response. Если нет, выводим ошибку
try:
    parsed_response_text = response.json()  # парсим ответ
    print(parsed_response_text)
except JSONDecodeError:
    print("Ответ не в формате JSON")
