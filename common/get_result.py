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
from common.global_dict import get_value, set_value


class GetResult():

    @staticmethod
    def get_result(data:dict,host=GetYml.getValue("/config/host.yml","baidu_manager_pc_test"),authorization=None,token=None) -> bool:
        no_login_headers = {
            "Authorization": None,
            "token": None
        }

        request_obj = data.get("request")

        uri = request_obj['uri']
        url = host+uri
        method = request_obj.get("method")
        print("")
        print("》》》》》》》》》》》》》》》》》》接口的请求信息》》》》》》》》》》》》》")
        print("接口的url:",url)
        print("接口的method:", method)

        # 对headers 的处理
        headers = request_obj.get("headers")
        print("headers", headers)
        # 替换
        headers=HandleStrUtils.replace_var(headers)
        print("headers",headers)
        print(type(headers))
        if authorization is not None:
            dict1={"Authorization": authorization}
            headers.update(dict1)

        if token is not None:
            dict3={"token": token}
            headers.update(dict3)

        print("接口的headers:", headers)

        # 获取请求参数，字典 datas
        datas = request_obj.get("datas")
        if datas is not None:
            datas = HandleStrUtils.replace_var(datas)

        # 依赖请求,替换传参数
        if "dependence" in data.keys():

            dependence_expectation_obj=GetResult.get_result_dependence(data,authorization=authorization,token=token,host=host)
            # 将请求参数的中的变量，替换为依赖接口的返回值。
            datas = HandleStrUtils.replace_dict_to_dict(datas, dependence_expectation_obj)
            print("有依赖接口，替换后的datas：",datas)
        else:
            pass



        print("接口请求的datas",datas)

        if "post" == method:
            # 将字典转化为json
            datas = json.dumps(datas)
            # 返回结果为json
            res = requests.request(method, url=url, data=datas, headers=headers)

        else:
            # get请求
            # params=datas 为字典
            res = requests.get(url, params=datas, headers=headers)

        print("接口的返回结果为：",res.json())

        # 提取接口的返回值，存到内存字典里
        if "export" in data.keys() and data.get("export") is not None:
            export_dict = data.get("export")
            HandleStrUtils.set_value_dict(export_dict, res.json())
        # 处理teardown接口
        if "teardown" in data.keys():
            GetResult.teardown(data,authorization=authorization,token=token,host=host,last_res=res.json())

        else:
            pass

        #
        if res.status_code ==200:
            # 断言
            res = res.json()
            # 断言信息
            if "assertion" in data.keys():
                assertion_list = data.get("assertion")
                b = AssertJud.assert_jud(assertion_list, res)
                return b
            else:
                return True
        else:
            # raise StatusException("{}请求报错".format(url))
            return False



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
        if dependence_datas is not None:
            # 对字典datas中，变量进行处理
            dependence_datas = HandleStrUtils.replace_var(dependence_datas)
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


    # 处理teardown 请求的接口
    @staticmethod
    def teardown(data: dict, authorization=None, token=None, host=None,last_res:str=None):
        no_login_headers = {
            "Authorization": authorization,
            "token": token
        }
        # 获取teardown
        teardown_info = data.get("teardown")
        teardown_request_obj = teardown_info.get("request")
        teardown_url = teardown_request_obj.get("uri")
        # 检查uri ,自动补全uri的host
        teardown_url = HandleStrUtils.check_url(teardown_url, host)

        teardown_method = teardown_request_obj.get("method")

        # 组装headers
        teardown_headers = teardown_request_obj.get("headers")
        teardown_headers.update(no_login_headers)

        # 从上一个接口的返回值，提取数据
        teardown_expectation_obj={}
        print("一：", last_res is not None)
        print("一：","expectation" in teardown_info.keys())
        if last_res is not None and "expectation" in teardown_info.keys():
            if teardown_info.get("expectation") is None:
                print("........")
                teardown_expectation_obj = {}
            else:
                # 获取期望值
                teardown_expectation_obj = teardown_info.get("expectation")
                print("teardown数据中的teardown_expectation_obj：",teardown_expectation_obj )
                # 将字典中的$.data.list[0].id 转化为 dependence_res 中的实际值
                # 遍历字典
                for key, value in teardown_expectation_obj.items():
                    expectation_value = jsonpath.jsonpath(last_res, value)[0]
                    expectation_value = str(expectation_value)
                    # 替换值
                    teardown_expectation_obj[key] = expectation_value



        # 组装datas
        print("从上一个接口获取的datas:",teardown_expectation_obj )
        teardown_datas = teardown_request_obj.get("datas")
        if teardown_datas is not None:
            # 对字典datas中，变量进行处理
            teardown_datas = HandleStrUtils.replace_var(teardown_datas)

        # 将上一个接口获取的值，与datas组装。
        teardown_datas.update(teardown_expectation_obj)

        # 将请求 teardown_datas ，由字典，转换为json
        teardown_datas = json.dumps(teardown_datas)

        # 发送请求：
        print("》》》》》》》》》》》》》》teardown接口的请求信息》》》》》》》》》》》》》》》》")
        print("teardown_url", teardown_url)
        print("teardown_method", teardown_method)
        print("teardown_headers", teardown_headers)
        print("teardown_datas", teardown_datas)
        try:
            # 接口返回值
            teardown_res = requests.request(teardown_method, url=teardown_url, data=teardown_datas,
                                            headers=teardown_headers).json()
            if teardown_res.get("data") == None:
                raise ValueException("依赖接口的返回数据异常:{}".format(teardown_res))
        except Exception as e:
            raise StatusException("依赖接口的请求失败:{}".format(e))

        print("teardown接口返回值：", teardown_res)








