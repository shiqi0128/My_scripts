"""
-------------------------------------------------
  @Time : 2020/5/27 2:04 
  @Auth : 十七
  @File : lm_02_read_yaml.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
import yaml

with open("testcase.yml", encoding="utf-8") as file:
    # 用full_load方法去加载
    # 第二个参数为文件对象，读取出来是字典
    data = yaml.full_load(file)
