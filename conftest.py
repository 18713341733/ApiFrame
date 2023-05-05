'''
pytest中的预置函数配置文件，conftest文件名是固定的
所有测试用例执行之前先执行这个函数
'''
import pytest

from common.get_login_info import GetLoginInfo


# 获取用户登录信息的鉴权
@pytest.fixture(scope='session')
def get_authorization() ->str:
    authorization = GetLoginInfo.get_authorization()
    return authorization


# 全局大字典，所有的信息都可以放在这个里面
@pytest.fixture(scope='session')
def get_authorization() ->str:
    authorization = GetLoginInfo.get_authorization()
    return authorization
