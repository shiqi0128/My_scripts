"""
-------------------------------------------------
  @Time : 2020/5/28 0:29 
  @Auth : 十七
  @File : handle_yaml.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
import yaml

class HandleYaml:

    def __init__(self, filename=None):
        if filename is None:
            filename = "testcase.yml"
        else:
            filename = filename
        with open(filename, encoding="utf-8") as file:
            self.config_data = yaml.full_load(file)

    def get_data(self, section, option):
        """
        读取配置文件数据
        :param section:区域名
        :param option:选项名
        :return:值
        """
        return self.config_data[section][option]


do_yaml = HandleYaml()

if __name__ == '__main__':
    do_yaml = HandleYaml()
    print(do_yaml.get_data("api", "api_version"))
