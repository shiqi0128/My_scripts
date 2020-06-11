
# 字符串 ==> json
a = '{"msg": "success", "data": "login success"}'

# 转化成字典
import json
b = json.loads(a)
print(b)
print(b['data'])


# "<p onclick="red_it(this)"> hello world </p>"
# ===> dom.tagname  ==> p
# dom.text ==>  hello world
# dom.href ===> ...
# dom.value ==>>