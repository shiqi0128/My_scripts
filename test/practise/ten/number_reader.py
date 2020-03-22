import json

filename = r'F:\test\practise\ten\numbers.json'
with open(filename) as file_object:
    n = json.load(file_object)

print(n)