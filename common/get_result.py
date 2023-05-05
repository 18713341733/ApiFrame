# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 04 -24
# @File: get_result.py
# desc:
import json

import jsonpath
import requests

from common.get_yml import GetYml
from common.assert_jud import AssertJud
from common.my_exception import ValueException,StatusException
from common.handle_str_utils import HandleStrUtils
from common.my_exception import StatusException,ValueException

class GetResult():

    @staticmethod
    def get_result(data:dict,host=GetYml.getValue("/config/host.yml","baidu_manager_pc_test"),authorization=None,token=None) -> bool:
        no_login_headers = {
            "Authorization": authorization,
            "token": token
        }

        request_obj = data.get("request")
        # 断言信息
        assertion_list = data.get("assertion")
        uri = request_obj['uri']
        url = host+uri
        method = request_obj.get("method")
        print("")
        print("》》》》》》》》》》》》》》》》》》接口的请求信息》》》》》》》》》》》》》")
        print("接口的url:",url)
        print("接口的method:", method)

        headers = request_obj.get("headers")
        headers.update(no_login_headers)
        print("接口的headers:", headers)
        # 获取请求参数，字典 datas
        datas = request_obj.get("datas")

        # 对字典datas中，变量进行处理
        datas = HandleStrUtils.replace_var(datas)

        # 依赖请求,替换传参数
        if "dependence" in data.keys():

            dependence_expectation_obj=GetResult.get_result_dependence(data,authorization=None,token=token,host=host)
            # 将请求参数的中的变量，替换为依赖接口的返回值。
            datas =HandleStrUtils.replace_dict_to_dict(datas,dependence_expectation_obj)
            print("有依赖接口，替换后的datas：",datas)
        else:
            pass

        # 将字典转化为json
        datas = json.dumps(datas)
        print("接口请求的datas",datas)

        # 返回结果为json
        res = requests.request(method, url=url, data=datas, headers=headers)
        print("接口的返回结果为：",res.json())

        if res.status_code ==200:
            # 断言
            res = res.json()
            b = AssertJud.assert_jud(assertion_list, res)
            return b
        else:
            # raise StatusException("{}请求报错".format(url))
            return False


    # 百度咨询平台的接口，获取返回结果
    @staticmethod
    def get_result_bms(data:dict,host=GetYml.getValue("/config/host.yml","baidu_bms_test_baidu"),token=None) -> bool:
        b = GetResult.get_result(data,host,None,token)
        return b

    # 处理依赖接口的请求
    @staticmethod
    def get_result_dependence(data:dict,authorization=None,token=None,host=None) ->dict:
        no_login_headers = {
            "Authorization": authorization,
            "token": token
        }
        # 获取dependence
        dependence_info = data.get("dependence")
        dependence_request_obj = dependence_info.get("request")
        dependence_url = dependence_request_obj.get("uri")
        # 检查uri ,自动补全uri的host
        dependence_url=HandleStrUtils.check_url(dependence_url,host)

        dependence_method = dependence_request_obj.get("method")
        dependence_headers = dependence_request_obj.get("headers")
        dependence_headers.update(no_login_headers)

        # 将请求 dependence_datas ，由字典，转换为json
        dependence_datas = dependence_request_obj.get("datas")
        dependence_datas = json.dumps(dependence_datas)

        print("》》》》》》》》》》》》》》依赖接口的请求信息》》》》》》》》》》》》》》》》")
        print("dependence_url",dependence_url)
        print("dependence_method",dependence_method)
        print("dependence_headers",dependence_headers)
        print("dependence_datas",dependence_datas)
        try:
            # 接口返回值
            dependence_res = requests.request(dependence_method, url=dependence_url, data=dependence_datas,
                                              headers=dependence_headers).json()
            if dependence_res.get("data") == None:
                raise ValueException("依赖接口的返回数据异常:{}".format(dependence_res))
        except Exception as e:
            raise StatusException("依赖接口的请求失败:{}".format(e))

        print("依赖接口的返回值：",dependence_res)



        # 获取期望值
        dependence_expectation_obj = dependence_info.get("expectation")

        # 将字典中的$.data.list[0].id 转化为 dependence_res 中的实际值
        # 遍历字典
        for key,value in dependence_expectation_obj.items():
            expectation_value = jsonpath.jsonpath(dependence_res, value)[0]
            expectation_value = str(expectation_value)
            # 替换值
            dependence_expectation_obj[key] = expectation_value

        print("提取依赖接口的返回值：",dependence_expectation_obj)

        return dependence_expectation_obj







