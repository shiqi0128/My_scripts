#文件名是conftest.py
#conding=utf-8

import pytest


@pytest.fixture()
def myfixture():
    print("执行myfixture")