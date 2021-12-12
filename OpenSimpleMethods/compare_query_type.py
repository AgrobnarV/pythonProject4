import requests

response_true = requests.get("https://playground.learnqa.ru/api/compare_query_type")
print(response_true.text)

response_wrong = requests.post("https://playground.learnqa.ru/api/compare_query_type", params={"method": "HEAD"})
print(response_wrong.text)

response_put = requests.put("https://playground.learnqa.ru/api/compare_query_type", params={"method": "PUT"})
print(response_put.text)