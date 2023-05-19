# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -06
# @File: dependence_obj.py
# desc:

class DependenceObj:
    """"
    依赖请求的实例
    """

    def __init__(self,dependence_dic:dict):
        request_info = dependence_dic.get("request")
        self.uri = request_info["uri"]
        self.method = request_info["method"]
        self.datas=request_info["datas"]
        self.expectation=dependence_dic.get("expectation")

    def __str__(self):
        return "\n 依赖请求：\n uri:{},\n method:{},\n datas:{} \n expectation:{}".format(self.uri,self.method,self.datas,self.expectation)