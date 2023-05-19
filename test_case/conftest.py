'''
pytest中的预置函数配置文件，conftest文件名是固定的
所有测试用例执行之前先执行这个函数
'''
import pytest
from common.get_login_info import GetLoginInfo
from common.global_dict import set_value
import random

from config.dbConnectPool.db_all import get_baidu_manage_db_conn


@pytest.fixture(scope='session')
def get_authorization() ->str:
    authorization = GetLoginInfo.get_authorization()
    return authorization

# 获取用户登录信息的鉴权(测试项目平台）
@pytest.fixture(scope='session')
def get_authorization_and_token():
    info = GetLoginInfo.get_authorization_and_token()
    authorization = info[0]
    token = info[1]
    set_value("token",token)
    set_value("Authorization", token)
    return authorization,token



# 在执行项目代码之前，最先执行这个方法。autouse=True
@pytest.fixture(scope="session", autouse=True)
def setup():
    # TODO 在执行项目代码之前，最先执行这个方法
    print("启动建立数据库连接")
    # 测试项目资讯平台数据库连接
    baidu_manager_conn = get_baidu_manage_db_conn()
    print("===========开始执行项目===============")
    yield baidu_manager_conn
    print("关闭数据库连接")
    baidu_manager_conn.close()
