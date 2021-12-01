import requests

name = 'Andrew'
print('Hello from ' + name)

req2 = requests.get("https://playground.learnqa.ru/api/hello", data={"name": "string"})
print(req2.status_code, req2.text)
