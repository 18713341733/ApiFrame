# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -18
# @File: test_demo2.py
# desc: 普通的post请求，不依赖登录信息
import allure
import pytest
from common.get_yml import GetYml
from common.get_result import GetResult


class Test_Demo2:
    """
    类名必须以Test_开头
    """


    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/case_demo2.yml", "/baidu/login"))
    @allure.story("登录")
    def test_login(self,test_data:dict):
        b = GetResult.get_result(test_data)
        assert b == True


    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/case_demo2.yml", "/baidu/computer/computer"))
    @allure.story("依赖登录信息请求post")
    def test_pe_product_edit_stats(self, test_data: dict, get_authorization_and_token):
        b = GetResult.get_result(test_data, authorization=get_authorization_and_token[0],
                                 token=get_authorization_and_token[1])
        assert b == True

    @pytest.mark.parametrize("test_data",
                             GetYml.getValue("/data/case_demo2.yml", "/baidu/xxx/delete-xxx-abc"))
    @allure.story("get请求，依赖登录信息")
    def test_pe_product_delete_redis_fund(self, test_data: dict, get_authorization_and_token):
        b = GetResult.get_result(test_data, authorization=get_authorization_and_token[0],
                                 token=get_authorization_and_token[1])
        assert b == True