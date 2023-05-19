# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -18
# @File: test_demo3.py
# desc:
import allure
import pytest
from common.get_yml import GetYml
from common.get_result import GetResult
from common.global_dict import get_value,set_value


class Test_Demo3:

    def setup_class(self):
        """类的初始化"""
        # 设置全局变量
        set_value("test_id",2963)

    def teardown_class(self):
        pass

    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/case_demo3.yml", "/baidu/product/hello"))
    @allure.story("请求参数中存在变量，变量来自全局大字典")
    def test_baidu_adc_derf(self,test_data:dict,get_authorization_and_token):
        b = GetResult.get_result(test_data,authorization=get_authorization_and_token[0],token=get_authorization_and_token[1])
        assert b == True
