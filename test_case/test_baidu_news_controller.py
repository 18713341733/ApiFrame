# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -05
# @File: test_baidu_news_controller.py


import allure
import pytest
from common.get_yml import GetYml
from common.get_result import GetResult
from common.global_dict import get_value,set_value
import os

class Test_NewsController:

    def setup_class(self):
        """类的初始化"""
        pass


    def teardown_class(self):
        pass

    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/baidu_news_controller.yml", "/baidu/queryNewsList"))
    @allure.story("百度获取资讯列表")
    def test_baidu_query_news_list(self,test_data:dict,get_token_bms):
        b = GetResult.get_result_bms(test_data,token=get_token_bms)
        assert b == True

    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/baidu_news_controller.yml", "/baidu/getNum"))
    @allure.story("描述")
    def test_baidu_get_num(self,test_data:dict,get_token_bms):
        b = GetResult.get_result_bms(test_data,token=get_token_bms)
        assert b == True

    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/baidu_news_controller.yml", "/baidu/detailNews"))
    @allure.story("查询百度资讯详情")
    def test_baidu_detail_news(self,test_data:dict,get_token_bms):
        b = GetResult.get_result_bms(test_data,token=get_token_bms)
        assert b == True


