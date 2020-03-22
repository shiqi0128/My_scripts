#coding=utf-8
import unittest
import HTMLTestRunner
import time
import os
import smtplib
from common import readConfig
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
localReadConfig = readConfig.ReadConfig()

#用例目录
test_suite_dir = './test_case/'
#报告目录
report_dir = './report/'
now = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))
def creatsuite():
    testunit = unittest.TestSuite()
    #discover 方法定义
    discover = unittest.defaultTestLoader.discover(test_suite_dir, pattern = 'test_*.py', top_level_dir = None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

alltestnames = creatsuite()

#定义发送邮件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new


def send_mail(new_report,filename):
    '''
    :param new_report:获取最新的文件
    :param new_report_fail:获取最新的文件的路径
    :param now:当前生成报告的时间
    :return:

    :param sender 读取配置文件中发件人
    :param sendpwd 读取配置文件中发件人密码
    :param receiver 读取配置文件中收件人
    :return:
    '''

    sender = localReadConfig.get_email('sender')
    sendpwd = localReadConfig.get_email('sendpwd')
    receiver = localReadConfig.get_email('receiver')
    print(receiver)

    #获取报告文件：'related'43行
    f = open(new_report,'rb')
    body_main = f.read()

    msg = MIMEMultipart()
    # 邮件标题
    msg['Subject'] = Header('自动化测试报告','utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    #邮件内容
    text = MIMEText(body_main,'html','utf-8')
    msg.attach(text)

    #发送附件
    att = MIMEApplication(open(filename, 'rb').read())
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename = filename)
    msg.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(localReadConfig.get_smtp('smtp'))
    smtp.login(sender,sendpwd)

    #将receiver string类型转换成list
    # b = []
    # for n in str(receiver).split(","):
    #     b.append(n)
    # print(b)
    smtp.sendmail(sender,receiver.spilt(","),msg.as_string())


if __name__ == '__main__':

    filename = report_dir + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'接口测试报告',
        description=u'用例执行结果：')

    # 执行测试用例
    runner.run(alltestnames)
    fp.close()
    #搜索最新生成的文件
    new_report = new_report(report_dir)
    #发送邮件
    send_mail(new_report,filename)
