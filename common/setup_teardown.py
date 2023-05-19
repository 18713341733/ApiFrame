# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 05 -09
# @File: setup_teardown.py
# desc:

import json
import re

import jsonpath
import requests

from common.get_yml import GetYml
from common.assert_jud import AssertJud
from common.my_exception import ValueException,StatusException
from common.handle_str_utils import HandleStrUtils
from common.my_exception import StatusException,ValueException
from common.global_dict import get_value, set_value,has_key

class SetupTeardown:

    @staticmethod
    def request(file_path:str,api_name:str,host=None):
        if host is None:
            host = GetYml.getValue("/config/host.yml", "baidu_manager_pc_test")
        data = GetYml.getValue(file_path, api_name)[0]

        request_obj = data.get("request")

        uri = request_obj['uri']
        url = host+uri
        method = request_obj.get("method")
        print("")
        print("》》》》》》》》》》》》》》》》》》setup_teardown接口的请求信息》》》》》》》》》》》》》")
        print("接口的url:",url)
        print("接口的method:", method)

        # 对headers 的处理
        headers = request_obj.get("headers")
        # 替换
        headers=HandleStrUtils.replace_var(headers)

        print("接口的headers:", headers)
        # 获取请求参数，字典 datas
        datas = request_obj.get("datas")

        if datas is not None:
            for key, value in datas.items():
                var_list = re.findall(r"\$\{(.*?)\}", str(value))
                if len(var_list) > 0:
                    for i in var_list:
                        if not has_key(i):
                            return
            datas = HandleStrUtils.replace_var(datas)
        # 将字典转化为json
        datas = json.dumps(datas)
        print("接口请求的datas",datas)

        # 返回结果为json
        res = requests.request(method, url=url, data=datas, headers=headers)
        print("接口的返回结果为：",res.json())

        # 提取接口的返回值，存到内存字典里
        if "export" in data.keys() and data.get("export") is not None:
            export_dict = data.get("export")
            HandleStrUtils.set_value_dict(export_dict, res.json())

