# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 04 -26
# @File: test_goods_controller.py


import allure
import pytest
from common.get_yml import GetYml
from common.get_result import GetResult
from common.global_dict import get_value,set_value


class Test_GoodsController():
    """
    类名必须以Test_开头
    """
    def setup_class(self):
        """类的初始化"""
        # 设置全局变量，Goods的id
        set_value("id",113)

    def teardown_class(self):
        pass

    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/goods_controller.yml", "/Goods/getGoods"))
    @allure.story("获取Goods详细信息")
    def test_Goods_get_Goods(self,test_data:dict,get_token_bms):
        # 需要登录后的鉴权信息，要添加get_authorization
        print(">>>>>>>>>>>>>>>",get_token_bms)
        b = GetResult.get_result_bms(test_data,token=get_token_bms)
        assert b == True


    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/goods_controller.yml", "/Goods/queryGoodsList"))
    @allure.story("获取Goods列表")
    def test_Goods_query_Goods_list(self, test_data: dict,get_token_bms):

        # 需要登录后的鉴权信息，要添加get_authorization
        b = GetResult.get_result_bms(test_data, token=get_token_bms)
        assert b == True

    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/goods_controller.yml", "/Goods/getGoodsId"))
    @allure.story("xxxx")
    def test_goods_get_goods_id(self, test_data: dict,get_token_bms):

        b = GetResult.get_result_bms(test_data, token=get_token_bms)
        assert b == True


    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/goods_controller.yml", "/Goods/editGoods"))
    @allure.story("编辑Goods")
    def test_Goods_editGoods(self, test_data: dict,get_token_bms):

        b = GetResult.get_result_bms(test_data, token=get_token_bms)
        assert b == True

    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/goods_controller.yml", "/Goods/setGoodsStatus"))
    @allure.story("设置Goods状态")
    def test_Goods_set_Goods_status(self, test_data: dict, get_token_bms):
        b = GetResult.get_result_bms(test_data, token=get_token_bms)
        assert b == True