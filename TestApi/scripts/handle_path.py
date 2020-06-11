"""
-------------------------------------------------
  @Time : 2020/6/10 12:53 
  @Auth : 十七
  @File : handle_path.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: 1941816343@qq.com
-------------------------------------------------
"""
import os

# BASE_DIR = os.path.abspath(__file__)        # 查看当前文件的根路径(带当前文件名)
#
# two_path = os.path.dirname(BASE_URL)
#
# three_path = os.path.dirname(two_path)
# print(BASE_URL, two_path, three_path)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASE_PATH = os.path.join(BASE_DIR, 'cases')

CONF_PATH = os.path.join(BASE_DIR, 'confs')

CONF_FILE_PATH = os.path.join(CONF_PATH, 'testcase.yml')

DATA_PATH = os.path.join(BASE_DIR, 'data')

LOG_PATH = os.path.join(BASE_DIR, 'logs')

REPORTS_PATH = os.path.join(BASE_DIR, 'reports')

SCRIPTS_PATH = os.path.join(BASE_DIR, 'scripts')
pass
