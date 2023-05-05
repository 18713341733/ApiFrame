# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 04 -25
# @File: test_baidu_login_controller.py
# desc: 登录相关控制器


import allure
import pytest
from common.get_yml import GetYml
from common.get_result import GetResult


class Test_BaiduLoginController():
    """
    类名必须以Test_开头
    """
    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/baidu_login.yml", "/baidu/getInfo"))
    @allure.story("登录，获取角色权限")
    def test_baidu_get_info(self,test_data:dict,get_authorization):
        # 需要登录后的鉴权信息，要添加get_authorization
        b = GetResult.get_result(test_data,authorization=get_authorization)
        assert b == True

    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/baidu_login.yml", "/baidu/cap"))
    @allure.story("登录页面，获取验证码")
    def test_baidu_cap(self,test_data:dict):
        b = GetResult.get_result(test_data)
        assert b == True

    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/baidu_login.yml", "/baidu/login"))
    @allure.story("登录")
    def test_login(self,test_data:dict):
        b = GetResult.get_result(test_data)
        assert b == True