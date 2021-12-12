import requests

# без параметра метод
response_without_method = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"Метод без параметра {response_without_method.text}")
print()

# не описанный метод
payload_options = {"method": "OPTIONS"}
response_option = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload_options)
print(f"Не описанный метод {response_option.text}")
print()

# описанный метод - запрашиваем с post
payload = {"method": "POST"}
response_post = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
print(f"Ответ запроса {response_post.text} и статус запроса {response_post.status_code}")
print()

# проверяем значения реальных типов запроса и значений параметра method
method = {}
methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
for value in methods:
    method["method"] = value
    print(method)

    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
    print('get ' + response.text)

    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print('post ' + response.text)

    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print('put ' + response.text)

    response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print('head ' + response.text)

    response = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print('patch ' + response.text)

    response = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print('options ' + response.text)

    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
    print('delete ' + response.text)

    print()
    method = {}
