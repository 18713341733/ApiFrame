# -*- coding:utf-8 -*-
# @Author: 喵酱
# @time: 2023 - 04 -27
# @File: handle_str_utils.py
# desc: 处理、替换字字符串
import re

import jsonpath

from common.global_dict import get_value,set_value
import ast


class HandleStrUtils:

    # 完整的请求是一个dic datas
    # 替换的关键词也是一个字典 dependence_expectation_obj
    @staticmethod
    def replace_dict_to_dict(datas:dict,dependence_expectation_obj:dict) -> dict:
        datas.update(dependence_expectation_obj)
        return datas


    # 判断url字符串是否以http开头，如果不是的话，自动补全url
    @staticmethod
    def check_url(url:str,host:str) -> str:
        if url.startswith("http"):
            return url
        else:
            return host+url

    # post请求字典：处理请求datas中的变量，id: ${id}
    @staticmethod
    def replace_var(datas:dict) -> dict:
        for key, value in datas.items():
            var_list = re.findall(r"\$\{(.*?)\}", str(value))
            if len(var_list) > 0:
                for i in var_list:
                    expectation_value = get_value(i)
                    print(expectation_value)
                    # 替换字符串
                    pattern = r"\$\{" + i + r"\}"
                    print("替换变量的正则pattern：", pattern)
                    print("要被替换的value:", value)
                    value = re.sub(pattern, str(expectation_value), str(value))
                    print("result", value)

                    # 判断获取的数据类型
                    # 如果为int类型
                    if isinstance(expectation_value, int) and str(expectation_value) == str(value):
                        datas[key] = int(value)
                    else:
                        # 将value 字符串转成字典
                        try:
                            datas[key] = ast.literal_eval(value)
                        except:
                            datas[key] = value

        print("替换完变量后的datas:",datas)
        return datas

    #  将字典中的值，存到全局变量中
    @staticmethod
    def set_value_dict(export_dict: dict, res: str):
        # 遍历字典
        for key, value in export_dict.items():
            export_value = jsonpath.jsonpath(res, value)[0]
            export_value = str(export_value)
            # 提取的值放到内存里
            set_value(key, export_value)

    # get请求字符串：处理请求datas中的变量，"id=${id}"
    @staticmethod
    def replace_var_str(datas:str) -> str:
        var_list = re.findall(r"\$\{(.*?)\}", datas)
        if len(var_list) > 0:
            for i in var_list:
                expectation_value = get_value(i)
                print(expectation_value)
                # 替换字符串
                pattern = r"\$\{" + i + r"\}"
                print("替换变量的正则pattern：", pattern)
                print("要被替换的value:", datas)
                datas = re.sub(pattern, str(expectation_value), datas)
                print("result", datas)
        return datas

    # 判断sql的增删改查
    @staticmethod
    def check_sql_type(sql: str) -> str:
        pass


