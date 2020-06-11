"""
-------------------------------------------------
  @Time : 2020/5/29 17:23 
  @Auth : 十七
  @File : handle_log.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
import logging
from handle_yaml import do_yaml


class HandleLog:

    def __init__(self, name=None):
        if name is None:
            self.my_logger = logging.getLogger("testcase.log")
        else:
            self.my_logger = logging.getLogger(name)
        self.my_logger.setLevel(do_yaml.get_data("log", "logger_level"))        # 创建日志等级
        console_handler = logging.StreamHandler()          # 创建控制台输入日志
        console_handler.setLevel("DEBUG")                   # 创建控制台日志输出的等级

        if name is None:
            file_hander = logging.FileHandler(do_yaml.get_data("log", "log_filename"), encoding="utf-8")
        else:
            file_hander = logging.FileHandler(name, encoding="utf-8")       # 创建在文本日志里面的日志文件
        farmter = logging.Formatter('%(asctime)s - [%(levelname)s] - [msg]: %(message)s - %(name)s - %(lineno)d')
        console_handler.setFormatter(farmter)               # 将样式与日志器关联，用setFormater
        file_hander.setFormatter(farmter)
        self.my_logger.addHandler(console_handler)          # 日志对象与输出渠道关联
        self.my_logger.addHandler(file_hander)

    def get_logger(self):
        return self.my_logger

do_log = HandleLog().get_logger()

if __name__ == '__main__':
    do_log = HandleLog()
    my_logger = do_log.get_logger()
    my_logger.debug("这是一条debug级别的日志")
    my_logger.info("这是一条info级别的日志")
    my_logger.warning("这是一条waring级别的日志")
    my_logger.error("这是一条error级别的日志")
    my_logger.critical("这是一条critical级别的日志")


