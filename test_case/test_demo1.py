# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -18
# @File: test_demo1.py
# desc:
import allure
import pytest

from common.db_utils import DbUtils
from common.get_yml import GetYml
from common.get_result import GetResult
from common.global_dict import get_value,set_value

class Test_Demo1():

    @pytest.mark.parametrize("test_data", GetYml.getValue("/data/case_demo1.yml", "/baidu/test/study/max"))
    @allure.story("一个接口，写多条case")
    def test_baidu_get_study_max_sort(self, test_data: dict, get_authorization_and_token):
        b = GetResult.get_result(test_data, authorization=get_authorization_and_token[0],
                                 token=get_authorization_and_token[1])
        assert b == True


