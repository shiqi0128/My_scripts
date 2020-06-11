"""
-------------------------------------------------
  @Time : 2020/6/8 0:22 
  @Auth : 十七
  @File : handle_mysql.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
# import pymysql
#
# # 1、创建连接对象
# conn = pymysql.connect(host="api.lemonban.com",
#                 user="future",
#                 password="123456",
#                 port=3306,
#                 database="futureloan",
#                 charset="utf8",
#                 cursorclass=pymysql.cursors.DictCursor
#                 )
#
# # 2、创建游标对象
# one_cursor = conn.cursor()
#
# # 3、使用游标对象执行sql语句
# sql1 = 'SELECT *FROM member WHERE mobile_phone="13340346454"'
#
# # 4、执行sql
# one_cursor.execute(sql1)
#
# # 5、获取执行结果
# result = one_cursor.fetchone()
#
# # 6、关闭连接
# one_cursor.close()
# conn.close()




import pymysql

connct = pymysql.connect(host='api.lemonban.com',
                         user='future',
                         password='123456',
                         database='futureloan',
                         port='3306',
                         charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor
                         )

one_cursors = connct.cursor()

sql1='SELECT *FROM member WHERE mobile_phone="13340346454"'

one_cursors.execute(sql1)

result = one_cursors.fetchone()

one_cursors.close()
connct.close()

