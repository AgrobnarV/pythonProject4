import json

string2 = '{"answer": "key"}'
obj = json.loads(string2)
key = 'answer'
if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON не существует")
