import requests

response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "Andrew"})
print(response.text)
