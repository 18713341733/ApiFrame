'''
pytest中的预置函数配置文件，conftest文件名是固定的
所有测试用例执行之前先执行这个函数
'''
import pytest
from common.get_login_info import GetLoginInfo
from common.global_dict import get_value,set_value

# 获取用户登录信息的鉴权
@pytest.fixture(scope='session')
def get_authorization() ->str:
    authorization = GetLoginInfo.get_authorization()
    return authorization


# 获取用户登录信息的token
# 使用token有两种方式，方式1 pytest 提供的回调功能 方式2 全局变量
@pytest.fixture(scope='session')
def get_token_bms() ->str:
    token = GetLoginInfo.get_token_bms()
    # 将token写到全局变量里
    set_value("token", token)
    return token
