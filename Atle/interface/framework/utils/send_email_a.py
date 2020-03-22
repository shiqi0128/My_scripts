import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

my_sender = '1941816343@qq.com'  # 发件人邮箱账号
my_pass = '119920128xyz'  # 发件人邮箱密码
my_user = '862974339@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        msg = MIMEText('Python 邮件发送测试001...', 'plain', 'utf-8')
        msg['From'] = formataddr(["十七", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["Lucky_star", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login("1941816343@qq.com", "119920128xyz")  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail("1941816343@qq.com", ["862974339@qq.com", ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as ex:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(ex)
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")