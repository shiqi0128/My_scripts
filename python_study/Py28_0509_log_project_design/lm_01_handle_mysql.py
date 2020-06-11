# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/5/9 21:27 
  @Auth : 可优
  @File : lm_01_handle_mysql.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import pymysql

# 1、创建连接对象
conn = pymysql.connect(host="api.lemonban.com",
                       user="future",
                       password="123456",
                       port=3306,
                       database="futureloan",
                       charset="utf8",  # 不能为utf-8
                       # a.指定每一条记录为字典类型
                       # b.默认每一条记录为元祖类型
                       cursorclass=pymysql.cursors.DictCursor
                       )

# 2、创建游标对象
one_cursor = conn.cursor()

# 3、执行sql语句
# a.sql语句固定死了
# sql1 = 'SELECT * FROM member WHERE mobile_phone = "13734076707";'
# sql2 = 'SELECT * FROM member ORDER BY id DESC LIMIT 0,5;'

one_mobile = input("请输入您的手机号！")
# sql3 = f'SELECT * FROM member WHERE mobile_phone = {one_mobile};'
# b.给sql语句添加参数，%s为占位符

sql3 = 'SELECT * FROM member WHERE mobile_phone = %s;'

# one_cursor.execute(sql1)
# one_cursor.execute(sql2)
# one_cursor.execute(sql3)
# c.执行sql语句时，给sql语句传递参数，args为序列类型，参数与sql语句中的%s，一一对应
one_cursor.execute(sql3, args=[one_mobile])

# 4、获取值并提交
# fetchone获取一条数据，如果游标类为DictCursor，则结果为字典类型
# fetchall获取多条数据，如果游标类为DictCursor，则结果为嵌套字典的列表类型
result = one_cursor.fetchone()
# result = one_cursor.fetchall()
# 提交结果
conn.commit()

# 5、关闭连接
# a.必须先关游标
# b.再关连接
one_cursor.close()
conn.close()
























































