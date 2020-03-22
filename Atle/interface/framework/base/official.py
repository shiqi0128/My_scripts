# --------------------此文件为官网接口的基础文件-----------------------
import requests
from Atle.interface.framework.common.color import out_format

host = "http://csapp.aiitle.com:88"   # 测试服务器

class official():
    """定义一个官网接口的测试类"""
# 新闻模块
    def news_list(self):
        """新闻列表
        :param:size:单页记录数
        :param:page:页码
        """
        url = host + "/api/news/list"
        data = {"size": 10, "page": 1}
        r = requests.post(url=url, data=data).json()
        s = len(r["data"])
        if s == 0:
            print("data is NULL")
        else:
            out_format("新闻列表:", r)
            news_id = r["data"][-1]["id"]
            print("id", news_id)
            return news_id

    def news_details(self):
        """新闻详情
        :param:id:记录id
        """
        news_id = self.news_list()
        url = host + "/api/news/find"
        data = {"id" : news_id}
        r = requests.post(url=url, data=data).json()
        out_format("新闻详情:", r)

# 职位模块
    def work_list(self):
        """职位列表
        :param:size:单页记录数
        :param:page:页码
        """
        url = host + "/api/work/list"
        data = {"size": 10, "page": 1}
        r = requests.post(url=url, data=data).json()
        s = len(r["data"])
        if s == 0:
            print("data is NULL")
        else:
            out_format("职位列表:", r)
            work_id = r["data"][-1]["id"]
            print("id", work_id)
            return work_id

    def work_details(self):
        """职位详情
        :param:id:记录id
        """
        work_id = self.work_list()
        url = host + "/api/news/find"
        data = {"id": work_id}
        r = requests.post(url=url, data=data).json()
        out_format("职位详情:", r)


# official().news_list()
official().news_details()
# official().work_list()
official().work_details()
