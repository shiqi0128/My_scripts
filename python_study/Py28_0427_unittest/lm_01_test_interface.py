# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/4/27 20:15 
  @Auth : 可优
  @File : lm_01_test_interface.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from Py28_0427_unittest.handle_request import HandleRequest

# 1、构造请求参数
do_request = HandleRequest()
register_url = "http://api.lemonban.com/futureloan/member/register"

headers_dict = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "User-Agent": "Mozilla/5.0 LookSky"
}

do_request.add_headers(headers_dict)

request_param = {
    "mobile_phone": "18511112245",
    "pwd": "12345678"
}

# 2、发起请求
res = do_request.send("POST", register_url, json=request_param)

# 3、提取响应数据，然后断言结果
expected_value = 0
real_code = res.json()["code"]

if expected_value == real_code:
    print("恭喜您，测试成功，此接口没问题！")
else:
    print("不好意思，测试失败，此接口有问题！")


# 对其中一个反向用例进行测试
register_param1 = {
    "pwd": "12345678"
}

res1 = do_request.send("POST", register_url, json=register_param1)

expected_value1 = 1
real_code1 = res.json()["code"]

if expected_value1 == real_code1:
    print("恭喜您，测试成功，此接口没问题！")
else:
    print("不好意思，测试失败，此接口有问题！")


# 上面的测试过程有没有问题？ 痛点？
# 1、代码冗余严重
# 2、代码结构混乱
# 3、注册的手机号每次都要手动修改才不会重复
# 4、测试结果没有进行统计
# 5、没有日志记录功能，几乎不可能定位问题
