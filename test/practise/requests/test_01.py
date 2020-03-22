import requests
r = requests.head()
r = requests.get(url='https://www.baidu.com/', params=contents)
print(r.url)