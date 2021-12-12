import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
redirects = len(response.history)  # кол-во redirects_url

print(f"Кол-во редиректов, происходящих от изначальной точки назначения до итоговой -  {redirects}. Список: {response.history} ")
print(f"Итоговый url - {response.url}")

