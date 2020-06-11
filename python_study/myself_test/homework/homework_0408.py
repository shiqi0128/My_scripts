"""
-------------------------------------------------
  @Time : 2020/4/9 22:02 
  @Auth : 十七
  @File : homework_0408.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
# 一、必做题
# 1. __name__变量有什么特性？
# __name__是系统变量, 无需定义
# a. 如果运行当前模块, 那么__name__ 等于 __main__
# b. 如果当前模块是被其他py文件导入的, 那么__name__ 等于 模块名
# 2.os模块中有哪些常用的方法？用什么作用？
# 提示：演练一下
# os.getcwd():getcwd()方法显示当前的工作路径，只显示到具体路径，不具体显示到文件。
# os.path.join(a, b):链接2个部分的路径，组成一个完整的路径
# os.mkdir(路径名字):在某一个目录下创建一个新目录
# os.rmdir(路径名字):删掉一个目录
# os.listdir()：获取当前路径下的目录列表
# os.path.isdir:判断当前文件是否是目录，返回布尔值
# os.path.isfile:判断当前文件是否是文件，返回布尔值
# 3.文件有哪些种类？
# 常见抄文档格式有：TXT、DOC、EXCL、PPT、DOCX、XLSX、PPTX等
# 常见图片格式有：JPG、PNG、PDF、TIFF、SWF等
# 常见视频格式有：FLV、RMVB、MP4、MVB等
# 常见声音格式有：WMA、MP3等
# 常见系统度格式有：RAR、EXE等
# 4.文件的操作步骤
# 1)打开文件open()
# 2)读操作read()方法会将整个文件的内容全部读取出来
# 3)写操作write()
# 4)关闭文件close()
# 5.操作文件的常用函数/方法有哪些？
# 1)打开文件open()
# 2)读操作read()方法会将整个文件的内容全部读取出来
# 3)读操作readline()每次执行, 会读取一行内容
# 4)读操作readlines()会将每一行读取出来, 每一行作为列表的元素, 返回列表
# 5)mode文件操作模式,r,w,a:
# r+可读可写
# w+：打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a+：打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# 6)写操作write()
# 7)关闭文件close()
# 6.read、readline、readlines有什么区别？
# 提示：
# 	请从返回的对象类型、应用场景来阐述
# read()方法会将整个文件的内容全部读取出来，返回字符串类型
# readline()每次执行, 会读取一行内容，返回字符串类型
# readlines()会将每一行读取出来, 每一行作为列表的元素, 返回列表
# 7.编写如下程序
# 有两行数据，存放在txt文件里面：
# url:http://test.lemonban.com/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
# url:http://test.lemonban.com/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000
# 请利用所学知识，读取txt文件里面的两行内容，然后转化为如下格式（嵌套字典的列表）：（可定义函数）
# [{'url':'http://test.lemonban.com/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},{'url':'http://test.lemonban.com/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]
# 请自行copy数据到Python里面，进行完整的分析后，再进行程序的编写！


# def new_data():
#     file_list = []   # 用来存储临时结果
#     last_list = []   # 用来存放最终结果
#     one_file = open("lemon.txt", encoding="utf-8")     # 打开txt文件
#     result = one_file.read()                           # 读取txt文件
#     for item in result:
#         # 第一次以@来分隔
#         # ['url:http://test.lemonban.com/futureloan/mvc/api/member/register','mobile:18866668888', 'pwd:123456']
#         tmp_list = item.split("@")
#         for val in tmp_list:
#             # 第二次以:来分隔，只分隔一次
#             # [['url','http://test.lemonban.com/futureloan/mvc/api/member/register'],
#             # ['mobile', '18866668888'], ['pwd', '123456']]
#             file_list.append(val.split(":", 1))
#         last_list.append(dict(file_list))
#         # 将嵌套列表的列表转化为字典，然后添加到full_result_list中
#     # return last_list


# if __name__ == '__main__':
#     new_data()
#     res1 = result.split("@")    # 第一次以@来分隔
#     # print(f"res1:{res1}")
#     for item in res1:               # 遍历第一次按@分裂的列表
#         res2 = item.split(":", 1)     # 第二次按遍历出来的字符串根据第一个：再次分裂
#         file_list.append(res2)        # 分裂出来的字符串添加到存放最终结果的列表中
#     last_list.append(dict(file_list))       # 把列表类型变为字典类型
#     last_list.remove()
#     print(f"last_list:{last_list}")
#
#
# if __name__ == '__main__':
#     new_data()

def new_data():
    file_list = []   # 用来存储临时结果
    last_list = []   # 用来存放最终结果
    one_file = open("lemon.txt", encoding="utf-8")     # 打开txt文件
    result = one_file.readlines()                           # 读取txt文件
    # print(f"result:{result}\n类型:{type(result)}")
    for item in result:                                 # 遍历读取txt文件返回的列表
        res1 = item.strip("\n").split("@")              # 遍历的数据去掉第一次遍历的字符串末尾的\n换行符，再以@分隔
        # print(f"res1:{res1}\n类型：{type(res1)}")
        for val in res1:                                # 分隔后的结果是列表形式返回，再遍历这个返回的列表
            res2 = val.split(":", 1)                    # 以：分隔，根据第一次出现的：分隔
            file_list.append(res2)                      # 分隔后的列表添加进一个上面定义过的空列表
            # print(f"res2:{res2}\n类型：{type(res2)}")
            # print(f"file_list:{file_list}\n类型：{type(file_list)}")
        last_list.append(dict(file_list))               # 把列表类型变为字典类型
    print(f"last_list:{last_list}\n类型：{type(last_list)}")






    # print(f"res0:{res0}\n类型：{type(res0)}")
    # res1 = res0.split(" ")
    # print(f"res1:{res1}")
    # for val in res1:
    #     res3 = val.split("@")            # 第2次以@来分隔
    #     file_list.append(res3)
    #     print(f"res3:{res3}")
    #     for item in file_list:               # 遍历按@分隔的列表
    #         res4 = item.split(":", 1)     # 按遍历出来的字符串根据第一个：再次分隔
    #         print(f"res4:{res4}\n类型：{type(res4)}")
    #         file_list.append(res4)        # 分隔出来的字符串添加到存放最终结果的列表中
    #     last_list.append(dict(file_list))       # 把列表类型变为字典类型
    #     print(f"last_list:{last_list}")


if __name__ == '__main__':
    new_data()



# res2 = "".join(res1)
# print(f"res2:{res2}")
# res3 = res2.split(":")
# print(f"res3:{res3}")
# # res4 =
# one_file.close()

# def handle_data(one_list):
#     """
#     将字符串切割之后，转换为字典
#     :param one_list:[str]
#     :return:字典
#     """
#     full_result_list = []  # 用于存储最终结果
#     tmp_result_list = []  # 用于存储临时结果
#     for item in one_list:
#         # 第一次以@来分隔
#         # ['url:http://test.lemonban.com/futureloan/mvc/api/member/register','mobile:18866668888', 'pwd:123456']
#         tmp_list = item.split("@")
#         for val in tmp_list:
#             # 第二次以:来分隔，只分隔一次
#             # [['url','http://test.lemonban.com/futureloan/mvc/api/member/register'],
#             # ['mobile', '18866668888'], ['pwd', '123456']]
#             tmp_result_list.append(val.split(":", 1))
#         full_result_list.append(dict(tmp_result_list))
#         # 将嵌套列表的列表转化为字典，然后添加到full_result_list中
#     return full_result_list
#
#
# def read_file_lines():
#     """
#     读取文件
#     :param file_path: 文件路径
#     :param mode: 文件打开模式
#     :param encoding: 文件编码
#     :return: [str]
#     """
#     # 打开文件
#     one_file = open("lemon.txt", mode="r", encoding="utf-8")
#     # 读取文件
#     file_lines_list = one_file.readlines()
#     for key, value in enumerate(file_lines_list):  # 将列表中每一行末尾的\n去除
#         file_lines_list[key] = value[:-1]
#     # 关闭文件
#     one_file.close()
#     return file_lines_list
#
#
# def main():
#     """
#     启动函数
#     :return:
#     """
#     completed_data = handle_data(read_file_lines("lenmon.txt"))
#     print("最终处理的数据为：\n{}".format(completed_data))
#
#
# if __name__ == '__main__':
#     main()




# 二、选作题
# 1.编写如下程序
# 创建一个txt文本文件，以csv格式（数据之间以英文逗号分隔）来添加数据
# a.第一行添加（写入）如下内容：
# name,age,gender,hobby,motto
# b.从第二行开始，每行添加（写入）具体信息，例如：
# 可优,17,男,臭美,Always Be Coding!
# 柠檬小姐姐,16,女,可优,Lemon is best!
# c.具体用户信息要求来自于一个嵌套字典的列表（请自定义这个列表，随意定义即可），例如：
# person_info = [{"name": "可优",
#                "age": 17,
#                "gender": "男",
#                "hobby": "臭美",
#                "motto": "Always Be Coding!"},
#               {"name": "柠檬小姐姐",
#                "age": 16,
#                "gender": "女",
#                "hobby": "可优",
#                "motto": "Lemon is best!"},
#               ]
# d.将所有用户信息写入到txt文件中之后，然后再读出