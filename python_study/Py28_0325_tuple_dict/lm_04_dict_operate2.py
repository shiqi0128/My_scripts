# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/3/25 21:27 
  @Auth : 可优
  @File : lm_04_dict_operate2.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
one_dict = {"id": 1, "title": "登录接口正向用例", "username": "云", "password": "8888",
            "expected": "登录成功", "is_excuted": True}

# 1. 修改字典的中值
# 2. 如果key存在, 那么会修改
# 3. 如果key不存在, 那么会创建一个键值对
# one_dict["id1"] = 10001

# 4. 使用update方法来合并两个字典
# 如果update方法参数字典中, 有相同的key, 那么会覆盖源字典中的键值对
# 如果update方法参数字典中, 不相同的key, 那么会合并
# two_dict = {True: "正确", None: "空值", "id": 10001}
# one_dict.update(two_dict)
# print(f"值为: {one_dict}\n类型为: {type(one_dict)}")
# print(f"值为: {two_dict}\n类型为: {type(two_dict)}")

# 5. 使用pop方法, 将指定的键值对删除, 同时会返回删除的这个key对应的值
# result = one_dict.pop("id")
# print(f"值为: {result}\n类型为: {type(result)}")
# print(f"值为: {one_dict}\n类型为: {type(one_dict)}")

# 6. clear清空一个字典
# one_dict.clear()
# print(f"值为: {one_dict}\n类型为: {type(one_dict)}")

# values() 获取所有的value值, 是一个生成器对象, 测试开发会学
# result = list(one_dict.values())
# result = tuple(one_dict.values())
result = tuple(one_dict.keys())
print(f"值为: {result}\n类型为: {type(result)}")

# 1. 正常情况下, py程序, 是从上到下执行的
# 2. 在你想让程序停止的左侧(行号栏), 鼠标单击, 红点点叫做断点
# 3. debug调试的好处(80% 时间在排错, 20%写代码)
#  a. 排除
#  b. 帮助理解程序
#  c. 研究源码
