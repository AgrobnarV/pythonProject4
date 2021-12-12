import requests

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"name1": "text1"})
print(response.text)

#баг 1 - сервер принимает port и params
#баг 2 - нет ответа для метода head
