# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -19
# @File: test_demo5.py
# desc:

import allure
import pytest
from common.get_yml import GetYml
from common.get_result import GetResult
from common.global_dict import get_value,set_value,has_key
from common.setup_teardown import SetupTeardown


class Test_Demo5r:

    def setup_class(self):
        """类的初始化"""
        # 设置id
        set_value("baidu_key_dict_id",54)
        # 设置id
        set_value("baidu_key_dict_id","151422")
        # 创建字典
        SetupTeardown.request("/data/case_demo5.yml", "setup_teardown_/baidu/baidu/baidu/edit-status")


    def teardown_class(self):
        # 删除字典
        SetupTeardown.request("/data/case_demo5.yml", "setup_teardown_/baidu/baidu/baidu/deleted")
