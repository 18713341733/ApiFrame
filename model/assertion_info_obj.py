# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -06
# @File: assertion_info_obj.py
# desc:

class AssertionInfoObj:
    """
        assertion:
      -
        - expectation: "操作成功"
        - compare: "in"
        - ctual_value:
    """

    def __init__(self,expectation,compare,ctual_value=None):
        self.expectation=expectation
        self.compare=compare
        self.ctual_value=ctual_value

