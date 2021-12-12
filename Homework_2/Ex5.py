import json

string = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this ' \ 
         'is a second message","timestamp":"2021-06-04 16:41:01"}]} '
json = json.loads(string)
key1 = "messages"
key2 = "message"
print(json[key1][1][key2])  # выводим сообщение второго массива
