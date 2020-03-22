"""此文件为gmall的PC端巡店逻辑所有 接口测试文件"""
import unittest
import requests
import json
import os
import random
from time import sleep
from interfaceTest.GMALL.gmall_header import host, get_header_pc
from interfaceTest.GMALL.gmall_all.color import out_format
from interfaceTest.GMALL.public_files import user_id, user_id_01
from urllib3 import encode_multipart_formdata
from datetime import datetime, timedelta

header, token1 = get_header_pc("admin_sylvia", "admin1")
header_xun, token2 = get_header_pc("admin80473", "admin@123")
header_zheng, token3 = get_header_pc("admin38796", "admin@123")


def Problem_list():
    """问题分类--列表
    :param:parent_id:父级id，非必填
    """
    url = host + "/api/company/patrol-issues"
    r = requests.get(url=url, headers=header).json()
    out_format("问题分类-列表:", r)
    problem_third_id = r["data"]["issues"][0]["children"][0]["children"][0]["id"]
    print("problem_third_id:", problem_third_id)
    return problem_third_id


problem_third_id = Problem_list()


def Record_list():
    """操作巡查记录 - 巡查记录列表
    :param:filter_type:类型 1：我的待办 2：我的已办 3：我创建的---必填
    :param:start_date:开始日期
    :param:end_date:结束日期
    :param:status:状态 0：未巡查 5：需整改 10：待验收 98：整改完成 99：已巡查 （不传为不限状态）
    :param:shop_id:门店id （不传为不限门店）
    :param:source:来源1:在线巡店 2:智能巡店（不传为不限来源）
    :param:page:页码
    :param:date_range_type:日期范围类型 1:当日 2:本周 3:本月 4:上月 5:更早以前
    """
    # sleep(60)
    url = host + "/api/company/patrol-tasks"
    data = {"filter_type": 1}
    r = requests.get(url=url, headers=header_xun, params=data).json()  # 1)巡查人查看我的创建，登录身份应该是创建人，不是巡查人2)变更整改人的时候登录身份应该是整改人的身份，且要查看【我的待办】，即状态未【需整改】
    out_format("操作巡查记录 - 巡查记录列表(我的创建)", r)  # 调用list函数转化为列表，不然输出结果会多一个dict.keys
    taskId = r["data"][1]["id"]
    return taskId
    # form_data = [
    #                 {"我的待办": ["1"]}, {"我的已办": ["2"]}, {"我创建的": ["3"]}
    #             ],
    # for data in form_data:
    #     # print(data)
    #     for data2 in data:
    #         print(data2.values())
    #         form_data_01 = {"filter_type": data2.values(), "page": "1"}
    #         r = requests.get(url=url, headers=header_xun, params=form_data_01).json()
    #         out_format("操作巡查记录 - 巡查记录列表--%s" % list(data2.keys()), r)  # 调用list函数转化为列表，不然输出结果会多一个dict.keys
    #         taskId = r["data"]["task"]["id"]
    #         return taskId


taskId = Record_list()

class Cruise_logic(unittest.TestCase):
    """定义一个巡店逻辑所有接口的 测试类"""

    def Problem_creat(self):
        """问题分类--创建
        :param:parent_id:父级id
        :param:content:巡查名称----必填
        :param:children:巡查项和问题----若添加巡查项时，会添加巡查问题 ，json中为巡查问题 children为json串，格式如下：
[
{"content": "\u684c\u9762\u6bd4\u8f83\u810f"},
{"content": "\u684c\u9762\u6bd4\u8f83\u810f"},
{"content": "\u684c\u9762\u6bd4\u8f83\u810f"}
]
1. 当添加巡查大类时，parent_id参数，请填写 0， children为空
2. 当添加巡查项和巡查问题时，parent_id 为要添加的巡查大类id，children不能为空，格式看“请求参数”
        """
        url = host + "/api/company/patrol-issues"
        data = {"parent_id": 0, "content": "鸡脚旮旯2"}       # 创建巡查大类
        r = requests.post(url=url, headers=header, json=data).json()
        out_format("添加巡查大类:", r)
        parent_id = r["data"]["issues"]["id"]
        print("巡查项大类的id:%s:" % parent_id)
        data2 = {
            "parent_id": r["data"]["issues"]["id"],
            "content": "门背后",
            "children": json.dumps([
                {
                    "content": "有垃圾"
                }
            ])
        }     # 创建巡查项,强制转义用json.dumps
        print(data2)
        r2 = requests.post(url=url, headers=header, json=data2).json()
        out_format("添加巡查项和问题:", r2)
        problem_id = r2["data"]["issues"]["id"]
        print("巡查项和问题的id:%s" % problem_id)
        return parent_id, problem_id

    def Problem_update(self):
        """问题分类-更新
        :param:content：待更新的数据
        :param:children:--json:修改项，格式如下[
{"id":"39","content":"\u684c\u9762\u6bd4\u8f83\u810f"}]
1. 若修改巡查大类，children无需填写
2. 若修改巡查项，children必填， children 中分为三个字段 第一个是id 代表巡查问题id 第二个是content代表要修改的巡查问题 第三个children 代表无限级
3. 若children中只有一个字段content，代表此数据为新增，若存在id，代表修改该id对应问题
        """
        parent_id_new, problem_id_new = self.Problem_creat()
        list_p = [parent_id_new, problem_id_new, ]
        form_data = [
            {"修改巡查大类": {"content": "沙发底下"}},
            {"修改巡查项&问题":
                {
                    "content": "门背后",
                    "children":
                        json.dumps(
                            [
                                {"id": problem_id_new,
                                 "content": "有垃圾"
                                 }
                            ]
                        )
                }
            }

        ]
        for index, p_id in enumerate(list_p):
            url = host + "/api/company/patrol-issues/%s" % p_id
            print("---", url)
            for data1 in form_data[index]:
                print("data1", data1)
                print("---", form_data[index][data1])
                r = requests.put(url=url, headers=header, json=form_data[index][data1]).json()
                out_format("问题分类-更新%s" % data1, r)
            # for data in form_data:
            #     for da in data:
            #         print("1111", data[da]["parent_id"])
            #         r = requests.put(url=url, headers=header, json=data[da]).json()
            #         out_format("问题分类-更新%s" % da, r)
            # data = {"修改巡查大类": {"parent_id": parent_id_new, "content": "沙发底下"}}
            # r = requests.put(url=url, headers=header, json=data).json()
        # out_format("问题分类-更新%s" % data, r)

    def Problem_delete(self):
        """问题分类--删除"""
        parent_id_new, problem_id_new = self.Problem_creat()
        list_p = [problem_id_new, parent_id_new]        # 必须先删除巡查项和问题才能删除巡查大类
        print(list_p)
        for p in list_p:
            url = host + "/api/company/patrol-issues/%s" % p
            r = requests.delete(url=url, headers=header).json()
            out_format("问题分类--删除:", r)

    def Patrol_add(self, start_date, end_date):
        """巡查计划--新增
        :param:start_date:任务开始时间
        :param:end_date:任务结束时间
        :param:name:任务名称
        :param:snapshot_ats:抓拍时间段,传数组形式
        :param:camera_ids:摄像头id 集合,传数组形式----注意，这里填的是camera的id不是code
        :param:patroller_uid:巡查人id
        :param:cycle:周期 0、1、2、3、4、5、6分别对应周日至周六, 传数组形式
        """
        url = host + "/api/company/patrol-schedules"
        ti = datetime.now() + timedelta(minutes=1)
        data = {
            "start_date": start_date, "end_date": end_date,
            "name": "检查垃圾桶%s" % random.randrange(1, 10000),
            "snapshot_ats":
                [ti.strftime("%Y-%m-%d %H:%M")],
            "camera_ids": ["64"],
            "patroller_uid": user_id,
            "cycle": ["1", "2", "3"]
        }
        r = requests.post(url=url, headers=header, json=data).json()
        out_format("巡查计划--新增:", r)
        scheduleId = r["data"]["schedule"]["id"]   # 巡查任务id， 下面的巡查详情需要调用
        print("scheduleId:", scheduleId)
        return scheduleId

    def Patrol_list(self):
        """巡查计划--列表"""
        url = host + "/api/company/patrol-schedules"
        r = requests.get(url=url, headers=header).json()
        out_format("巡查计划--列表:", r)

    def Patrol_detail(self):
        """巡查计划--详情
        :param:scheduleId:巡查计划id
        """
        scheduleId_01 = self.Patrol_add("2019-03-01", "2019-03-10")
        url = host + "/api/company/patrol-schedules/%s" % scheduleId_01
        i = 1
        while i <= 5:
            try:
                r = requests.get(url=url, headers=header).json()
                self.assertEqual(r["code"], 0)
                out_format("巡查计划--详情:", r)
                return scheduleId_01
            except:
                url_01 = host + "/api/company/patrol-schedules/%s" % scheduleId_01
                r = requests.patch(url=url_01, headers=header).json()
                out_format("巡查计划 - 修改状态", r)
            i +=1

    def Patrol_edit(self, start_date, end_date):
        """巡查计划--修改
        :param:start_date:任务开始时间
        :param:end_date:任务结束时间
        :param:name:任务名称
        :param:snapshot_ats:抓拍时间段,传数组形式
        :param:camera_ids:摄像头id 集合,传数组形式
        :param:patroller_uid:巡查人id
        :param:cycle:周期 0、1、2、3、4、5、6分别对应周日至周六, 传数组形式
        """
        scheduleId_02 = self.Patrol_detail()
        url = host + "/api/company/patrol-schedules/%s" % scheduleId_02
        data = {
            "start_date": start_date, "end_date": end_date,
            "name": "222",
            "snapshot_ats":
                ["08:30", "10:30"],
            "camera_ids": ["64", "65", "66"],
            "patroller_uid": user_id,
            "cycle": ["1", "2", "3"]
        }
        r = requests.put(url=url, headers=header, json=data).json()
        out_format("巡查计划--修改", r)
        return scheduleId_02

    # def Patrol_delete(self):
    #     """巡查计划--删除
    #     :param:scheduleId:巡查计划id
    #     """
    #     scheduleId_03 = self.Patrol_edit("2019-03-01", "2019-03-20")
    #     url = host + "/api/company/patrol-schedules/%s" % scheduleId_03
    #     r = requests.delete(url=url, headers=header).json()
    #     out_format("巡查计划--删除:", r)
    #     return scheduleId_03

    def Record_creat(self):
        """操作巡查记录 - 创建巡查记录
        :param:camera_id:摄像头id
        :param:issue_id:问题id，只需要填第三级问题id即可
        :param:comment:评论
        :param:corrector_uid:整改人uid
        :param:img_urls[]:图片列表，数组形式传参
        以上参数全部为必填
        """
        url = host + "/api/company/patrol-tasks"
        files = {"img_urls":
                     [
                        "http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%94%AF%E7%BE%8E%E5%9B%BE%E7%89%87&step_word=&hs=0&pn=56&spn=0&di=200640&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=2928956523%2C103323178&os=97091904%2C1424640616&simid=3108491783%2C3756554590&adpicid=0&lpn=0&ln=1701&fr=&fmq=1553832060056_R&fm=rs1&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=%E5%9B%BE%E7%89%87&objurl=http%3A%2F%2Fimg2.3lian.com%2F2014%2Ff4%2F95%2Fd%2F58.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bnstwg_z%26e3Bv54AzdH3F2tuAzdH3Fda89AzdH3Fab-8cAzdH3Fc00n8_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined"
                     ],
                 "camera_id": "64",
                 "issue_id": problem_third_id,
                 "comment": "角落里没打扫干净",
                 "corrector_uid": user_id_01,
                 }
        r = requests.post(url=url, headers=header, json=files).json()
        out_format("操作巡查记录 - 创建巡查记录:", r)

    def Record_detail(self):
        """操作巡查记录 - 巡查记录详情
        :param:taskId:巡查记录id--巡查列表返回的
        """
        url = host + "/api/company/patrol-tasks/%s" % taskId
        r = requests.get(url=url, headers=header).json()
        out_format("操作巡查记录 - 巡查记录详情:", r)

    def patrol(self):
        """操作巡查记录 - 巡查
        :param:taskId--巡查记录id,关联到创建巡查记录里面返回的id  索引为r["data"]["task"]["id"]
        :param:issue_id:问题id，只需要填第三级问题id即可，无需整改时不需要该字段，反之必须
        :param:need_correct:是否需要整改 0：否 1：是-----必填
        :param:comment:评论
        :param:corrector_uid:整改人uid，无需整改时不需要该字段，反之必须
        """
        # sleep(60)
        url = host + "/api/company/patrol-tasks/%s/inspect" % taskId
        data = {"need_correct": 1, "issue_id": problem_third_id, "corrector_uid": user_id_01}
        r = requests.put(url=url, headers=header_xun, json=data).json()
        out_format("操作巡查记录 - 巡查:", r)
        # 这个接口报错'巡查记录状态异常，请重新操作'的时候是因为在创建人-[智能巡查]-[我的创建]里面没有未巡查的记录，有未巡查的记录执行这个接口才会正确

    def rectify(self):
        """操作巡查记录 - 整改
        :param:img_urls[]:整改图片列表
        :param:snapshot_ats[]:整改图片时间列表，应该与 img_urls字段一一对应
        均是数组形式，均为必填
        """
        url = host + "/api/company/patrol-tasks/%s/correct" % taskId
        data = {
            "img_urls": [
                "http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%94%AF%E7%BE%8E%E5%9B%BE%E7%89%87&step_word=&hs=0&pn=39&spn=0&di=49170&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=2032309427%2C1487047270&os=708303973%2C2265263622&simid=3317853406%2C371925036&adpicid=0&lpn=0&ln=1701&fr=&fmq=1553832060056_R&fm=rs1&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=%E5%9B%BE%E7%89%87&objurl=http%3A%2F%2Fimg05.tooopen.com%2Fimages%2F20140515%2Fsy_61231773481.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bp555rjg_z%26e3Bv54AzdH3FetjoAzdH3Fm8dn80_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined"
            ],
            "snapshot_ats": ["2019-03-29 11:11:11"]
        }
        r = requests.put(url=url, headers=header_zheng, json=data).json()
        out_format("操作巡查记录 - 整改:", r)

    def alter_rectify(self):
        """操作巡查记录 - 变更整改人
        :param:corrector_uid:整改人id
        """
        url = host + "/api/company/patrol-tasks/%s/corrector" % taskId
        data = {"corrector_uid": "2369"}
        r = requests.put(url=url, headers=header_zheng, json=data).json()
        out_format("操作巡查记录 - 变更整改人:", r)
    #
    def accept(self):
        """操作巡查记录 - 验收
        :param:status:验收状态 1：通过 2：驳回
        """
        url = host + "/api/company/patrol-tasks/%s/accepting" % taskId
        data = {"status": "1"}
        r = requests.put(url=url, headers=header_xun, json=data).json()
        out_format("操作巡查记录 - 验收:", r)

    def inspect_statistical(self, start_date, end_date):
        """巡查统计
        :param:start_date:开始日期
        :param:end_date:结束日期
        """
        url = host + "/api/company/patrol-stats/dashboard"
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("巡查统计:", r)

    def inspect_problem(self, start_date, end_date):
        """巡查统计--巡查问题详情
        :param:start_date:开始日期
        :param:end_date:结束日期
        """
        url = host + "/api/company/patrol-stats/issue"
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("巡查统计--问题详情:", r)

    def inspect_rectify(self, start_date, end_date):
        """巡查统计 - 巡查整改详情
        :param:start_date:开始日期
        :param:end_date:结束日期
        :param:sort_field:排序字段1 : 整改任务总数; <br /> 2 ：整改中任务数;<br /> 3 ：整改完成任务数; <br /> 4：整改完成率
        :param:sort_type:排序值 asc ： 升序，desc ：倒序
        以上均为必填
        """
        url = host + "/api/company/patrol-stats/correct"
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "sort_field": "4",
            "sort_type": "desc"
        }
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("巡查统计--巡查整改详情:", r)

    def inspect_task(self, start_date, end_date):
        """巡查统计 - 巡查任务详情
        :param:start_date:开始日期
        :param:end_date:结束日期
        :param:sort_field:排序字段1:巡查任务数; <br /> 2:已巡查任务数;<br /> 3:未巡查任务数; <br /> 4:巡查整改中
        :param:sort_type:排序值 asc:升序，desc:倒序
        以上均为必填
        """
        url = host + "/api/company/patrol-stats/task"
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "sort_field": "2",
            "sort_type": "desc"
        }
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("巡查统计--巡查任务详情:", r)

    def comment_list(self):
        """巡查记录-评论列表
        :param:page:页码
        :param:target_type:目标类型 1：巡检记录
        :param:target_id:目标id
        :param:page_size:每页条数
        以上均为必填
        """
        url = host + "/api/comments"
        data = {"target_type": 1, "target_id": taskId}
        r = requests.get(url=url, headers=header, params=data).json()
        out_format("巡查记录--评论列表:", r)

    def comment_add(self):
        """巡查记录-添加评论
        :param:content:评论内容
        :param:replied_id:回复的评论id-----非必填
        :param:target_type:评论对象类型 1：巡查记录
        :param:target_id:评论对象id
        """
        url = host + "/api/comments"
        data = {"content": "努力再努力", "target_type": 1, "target_id": taskId}
        r = requests.post(url=url, headers=header, json=data).json()
        out_format("巡查记录--添加评论:", r)



# Cruise_logic().Problem_list()
# Cruise_logic().Problem_creat()
# Cruise_logic().inspect_update()
# Cruise_logic().inspect_delete()
# Cruise_logic().Patrol_list()
# Cruise_logic().Patrol_add("2019-03-01", "2019-04-30")
# Cruise_logic().Patrol_detail()
# Cruise_logic().Patrol_edit("2019-03-01", "2019-03-20")
# Cruise_logic().Patrol_delete()
# Cruise_logic().Record_creat()
# Cruise_logic().Record_list()
# Cruise_logic().Record_list()
# Cruise_logic().Record_detail()
# Cruise_logic().patrol()
# Cruise_logic().rectify()
# Cruise_logic().alter_rectify()
# Cruise_logic().accept()
Cruise_logic().inspect_statistical("2019-03-01", "2019-04-30")
Cruise_logic().inspect_problem("2019-03-01", "2019-04-30")
Cruise_logic().inspect_rectify("2019-03-01", "2019-04-30")
Cruise_logic().inspect_task("2019-03-01", "2019-04-30")
# Cruise_logic().Patrol_creat()
# Cruise_logic().inspect_statistical("2019-03-01", "2019-03-30")
Cruise_logic().comment_list()
Cruise_logic().comment_add()