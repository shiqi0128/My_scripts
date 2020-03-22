import urllib.request
from urllib import request
import ssl

response = request.urlopen(url, data=None, timeout=10)
doc = urlopen("http://www.baidu.com").read()
print(doc)
