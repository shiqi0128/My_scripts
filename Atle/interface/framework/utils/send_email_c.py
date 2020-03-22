# coding=utf-8
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。

# 3.导入unittest模块
import unittest
import os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
# 4.编写测试用例和断言
def all_case():
    # 待执行用例的目录
    # case_dir = "C:\\Users\\DELL\\PycharmProjects\\honggetest\\case"
    case_dir = os.path.join(os.getcwd(), "case")
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    # #discover方法筛选出用例，循环添加到测试套件中
    # for test_suit in discover:
    #     for test_case in test_suit:
    #         #添加用例到testcase
    #         testcase.addTests(test_case)
    # print(testcase)

    testcase.addTests(discover)  # 直接加载 discover    可以兼容python2和3
    print(testcase)
    return testcase


# ==============定义发送邮件==========
file_new = r"E:\script\Atle\interface\framework\Test_report"


def send_mail(file_new):   # file_new是测试报告路径的参数名
    f = open(file_new, "rb")
    mail_body = f.read()
    f.close()

    username = "十七"  # 发件箱用户名
    password = "119920128xyz"       # 发件箱密码
    sender = "1941816343@qq.com"   # 发件人邮箱
    receiver = ["862974337@qq.com"]  # 收件人邮箱
    # 邮件正文是MIMEText
    msg = MIMEText(mail_body, "html", "utf-8")
    # 邮件对象
    msg["Subject"] = Header("自动化测试报告", "utf-8").encode()
    msg["From"] = Header(u"测试机 <%s>" % sender)
    msg["To"] = Header(u"测试负责人 <%s>" % receiver)
    msg["date"] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect("smtp.mxhichina.com")  # 邮箱服务器
    smtp.login(username, password)  # 登录邮箱
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
    smtp.quit()
    print("邮件已发出！注意查收。")


# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)
    return file_new

if __name__ == "__main__":
    # 返回实例
    runner = unittest.TextTestRunner()
    # 导入第三方模块HTMLTestRunner
    import HTMLTestReportCN
    import time
    # 获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    # 保存生成报告的路径
    report_path =  "C:\\Users\\DELL\\PycharmProjects\\honggetest\\report\\"+now+"_result.html"
    fp = open(report_path,"wb")
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                             title=u"这是我的自动化测试用例",
                                             description=u"用例执行情况",
                                             verbosity=2
                                            )
    # run 所有用例
    runner.run(all_case())
    # 关闭文件，记住用open()打开文件后一定要记得关闭它，否则会占用系统的可打开文件句柄数。
    fp.close()
    # 测试报告文件夹
    test_path = "C:\\Users\\DELL\\PycharmProjects\\honggetest\\report\\"
    new_report = new_report(test_path)
    send_mail(new_report)  # 发送测试报告
