# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/5/8 20:58 
  @Auth : 可优
  @File : lm_02_read_yaml.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
# 安装第三方模块pyyaml
# 0、导入yaml模块
import yaml

# 1、打开yaml配置文件
with open("testcases.yaml", encoding="utf-8") as file:
    # full_load方法去加载
    # 第二个参数为文件对象
    # yaml.load_all(file, Loader=yaml.FullLoader)
    data = yaml.full_load(file)
    pass
