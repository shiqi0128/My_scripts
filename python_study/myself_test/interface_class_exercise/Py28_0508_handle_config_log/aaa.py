"""
-------------------------------------------------
  @Time : 2020/5/28 1:42 
  @Auth : 十七
  @File : aaa.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/5/8 21:36 
  @Auth : 可优
  @File : lm_03_handle_log.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import logging

# 1、创建Logger对象
# 相当于日志记录工具
my_logger = logging.getLogger("testcase")

# 2、设置日志器的日志等级
# 日志等级
# NOTSET(0), DEBUG(10), INFO(20), WARNING(30), ERROR(40), CRITICAL(50)
# 只能记录日志级别大于等于当前日志级别的日志
my_logger.setLevel("DEBUG")
# my_logger.setLevel(logging.DEBUG)

# 3、创建日志输出渠道（日志显示的地方）
console_handler = logging.StreamHandler()
console_handler.setLevel("WARNING")

file_handler = logging.FileHandler("testcase.log", encoding="utf-8")

# 4、创建日志的显示样式（格式）并与渠道进行关联
formater = logging.Formatter('%(asctime)s - [%(levelname)s] - [msg]: %(message)s - %(name)s - %(lineno)d')
console_handler.setFormatter(formater)
file_handler.setFormatter(formater)

# 5、日志器对象与日志输出渠道（展示的地方）进行关联
my_logger.addHandler(console_handler)
my_logger.addHandler(file_handler)


if __name__ == '__main__':
    # 手动产生不同级别的日志
    my_logger.debug("这是一条debug级别的日志！")
    my_logger.info("这是一条info级别的日志！")
    my_logger.warning("这是一条warning级别的日志！")
    my_logger.error("这是一条error级别的日志！")
    my_logger.critical("这是一条critical级别的日志！")
