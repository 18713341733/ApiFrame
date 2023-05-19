# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -18
# @File: test_demo4.py
# desc:
import allure
import pytest

from common.db_utils import DbUtils
from common.get_yml import GetYml
from common.get_result import GetResult
from common.global_dict import get_value,set_value
import os

from config.dbConnectPool.db_all import get_baidu_manage_db_conn


class Test_demo4:

    def setup_class(self):
        """类的初始化"""
        # 设置咨询的id
        set_value("id",1732)

        # 通过sql删除数据
        delete_news_sql = "delete from db_name.table_name where title='接口自动化测试自动删除';"
        DbUtils.execute_sql(get_baidu_manage_db_conn(), delete_news_sql)

    def teardown_class(self):
        # 删除banner
        delete_banner_sql = "delete from db_name.table_name where title='接口自动化测试自动删除';"
        DbUtils.execute_sql(get_baidu_manage_db_conn(), delete_banner_sql)


    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/case_demo4.yml", "/section/getName"))
    @allure.story("请求参数中存在变量，变量来自于另一个依赖接口")
    def test_section_detail_news(self,test_data:dict,get_authorization_and_token):
        b = GetResult.get_result(test_data, authorization=get_authorization_and_token[0],
                                 token=get_authorization_and_token[1])
        assert b == True


    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/case_demo4.yml",
                                                          "/create/good"))
    @allure.story("通过依赖接口实现teardown")
    def test_baidu_create_good(self, test_data: dict, get_authorization_and_token):
        b = GetResult.get_result(test_data, authorization=get_authorization_and_token[0],
                                 token=get_authorization_and_token[1])
        assert b == True